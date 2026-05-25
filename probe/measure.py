"""
读取 probe 固件通过 USB CDC 输出的 GPIO 电容数据。

用法:
    python measure.py              # 自动找 RP2040 CDC 口
    python measure.py --port COM7  # 指定端口
    python measure.py --flash probe.uf2  # 先拷 uf2 到 RPI-RP2 再等 CDC
"""
from __future__ import annotations
import argparse
import shutil
import sys
import time
from pathlib import Path

try:
    from serial import Serial
    from serial.tools import list_ports
except ImportError:
    print("pip install pyserial", file=sys.stderr)
    sys.exit(1)

RP2040_VID = 0x2E8A


def find_cdc_port() -> str | None:
    for p in list_ports.comports():
        if p.vid == RP2040_VID:
            return p.device
    return None


def find_rpi_rp2_mount() -> Path | None:
    for drive in "DEFGHIJKLMNOPQRSTUVWXYZ":
        info = Path(f"{drive}:/INFO_UF2.TXT")
        if info.exists():
            return Path(f"{drive}:/")
    return None


def wait_for(fn, desc: str, timeout: float = 30.0):
    print(f"waiting for {desc} ...", end="", flush=True)
    t0 = time.time()
    while time.time() - t0 < timeout:
        r = fn()
        if r:
            print(f" found ({r})")
            return r
        time.sleep(0.3)
        print(".", end="", flush=True)
    print(" timeout")
    return None


def classify(data: dict[str, int]) -> str:
    """根据签名粗判版本。仅基于"哪些 GPIO 明显有焊线"。"""
    # 取中位数做阈值，count > 阈值视作"焊了线"
    vals = sorted(data.values())
    threshold = max(vals[len(vals) // 4] * 3, 10)  # 保守一点
    wired = {p for p, v in data.items() if v > threshold}

    has = lambda *ps: all(f"GP{p}" in wired for p in ps)

    gp0 = "GP0" in wired
    gp26 = "GP26" in wired
    gp18_22 = any(f"GP{i}" in wired for i in range(18, 23))

    if has(0) and gp18_22 and not gp26:
        return "2x15 v2 (GP0 连续, 无 GP26)"
    if not gp0 and gp26 and gp18_22:
        return "2x15 v1 (有 GP26, GP0 空)"
    if not gp0 and not gp26 and not gp18_22 and has(12):
        return "5x6 (仅用到 GP1-17)"
    return f"未知签名, 焊线 GPIO: {sorted(wired, key=lambda s: int(s[2:]))}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", help="CDC 串口, 留空则自动查找")
    ap.add_argument("--flash", help="先把此 uf2 拷到 RPI-RP2 再等 CDC")
    ap.add_argument("--raw", action="store_true", help="只打印原始输出, 不分类")
    args = ap.parse_args()

    if args.flash:
        mount = wait_for(find_rpi_rp2_mount, "RPI-RP2 mount")
        if not mount:
            sys.exit(1)
        shutil.copy(args.flash, mount / Path(args.flash).name)
        print(f"copied {args.flash} -> {mount}")

    port = args.port or wait_for(find_cdc_port, f"CDC port (VID={RP2040_VID:#06x})")
    if not port:
        sys.exit(1)

    data: dict[str, int] = {}
    with Serial(port, 115200, timeout=5) as ser:
        time.sleep(0.3)
        ser.write(b"M\n")  # 请求一次新测量
        while True:
            line = ser.readline().decode("utf-8", errors="replace").strip()
            if not line:
                continue
            if args.raw:
                print(line)
            if line == "END":
                break
            if line.startswith("GP") and "," in line:
                pin, count = line.split(",", 1)
                try:
                    data[pin.strip()] = int(count.strip())
                except ValueError:
                    pass

    if not data:
        print("no data received"); sys.exit(1)

    # 打印表格 + 分类
    print()
    print(f"{'pin':<6}{'count':>8}   bar")
    max_v = max(data.values()) or 1
    for pin in sorted(data.keys(), key=lambda s: int(s[2:])):
        v = data[pin]
        bar = "#" * int(v * 50 / max_v)
        print(f"{pin:<6}{v:>8}   {bar}")

    print()
    print(f"猜测: {classify(data)}")


if __name__ == "__main__":
    main()
