"""让当前已刷 Vial 固件的板子跳进 BOOTSEL 模式 (出现 RPI-RP2 盘)."""
import sys
try:
    import hid
except ImportError:
    print("pip install hid"); sys.exit(1)

VID = 0x454C
sent = 0
for info in hid.enumerate(VID):
    if info['usage_page'] == 0xFF60 and info['usage'] == 0x61:
        print(f"-> {info['product_string']} (pid={info['product_id']:#06x})")
        d = hid.Device(path=info['path'])
        d.write(bytes([0x00, 0xFF]) + b'\x00' * 30)
        d.close()
        sent += 1

if sent == 0:
    print("no raw HID found. 板子没插? 或固件没开 RAW_ENABLE?", file=sys.stderr)
    sys.exit(1)
print(f"sent reset to {sent} device(s). RPI-RP2 盘应即将出现.")
