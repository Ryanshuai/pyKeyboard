#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * Layer 0: Normal (右手)
     * ┌────┬────┬────┬────┬────┬────┐
     * │ 6  │ 7  │ 8  │ 9  │    │    │
     * ├────┼────┼────┼────┼────┼────┤
     * │ Y  │ U  │ I  │ O  │ 0  │DEL │
     * ├────┼────┼────┼────┼────┼────┤
     * │ H  │ J  │ K  │ L  │ P  │ \  │
     * ├────┼────┼────┼────┼────┼────┤
     * │ N  │ M  │ ↑  │ .  │ ,  │ _  │
     * ├────┼────┼────┼────┼────┼────┤
     * │ =  │ ←  │ ↓  │ →  │ *  │ /  │
     * ├────┼────┼────┼────┼────┼────┤
     * │Fn1 │Ctrl│Alt │GUI │Shft│C+F8│
     * └────┴────┴────┴────┴────┴────┘
     */
    [0] = LAYOUT(
        KC_6,    KC_7,    KC_8,    KC_9,    KC_NO,   KC_NO,
        KC_Y,    KC_U,    KC_I,    KC_O,    KC_0,    KC_DEL,
        KC_H,    KC_J,    KC_K,    KC_L,    KC_P,    KC_BSLS,
        KC_N,    KC_M,    KC_UP,   KC_DOT,  KC_COMM, S(KC_MINS),
        KC_EQL,  KC_LEFT, KC_DOWN, KC_RGHT, KC_PAST, KC_SLSH,
        MO(1),   KC_LCTL, KC_LALT, KC_LGUI, KC_LSFT, C(KC_F8)
    ),

    /*
     * Layer 1: Fn1 (右手) - 根据截图更新
     * ┌────┬────┬────┬────┬────┬────┐
     * │ F7 │ F8 │ F9 │F10 │    │    │
     * ├────┼────┼────┼────┼────┼────┤
     * │Sft*│Sft(│Sft)│ O  │F11 │F12 │
     * ├────┼────┼────┼────┼────┼────┤
     * │Sft{│Sft}│    │ L  │ P  │ |  │
     * ├────┼────┼────┼────┼────┼────┤
     * │Sft[│PgUp│ >  │ <  │Sft-│    │
     * ├────┼────┼────┼────┼────┼────┤
     * │ :  │Home│PgDn│End │ *  │Sft/│
     * ├────┼────┼────┼────┼────┼────┤
     * │    │    │    │    │    │    │
     * └────┴────┴────┴────┴────┴────┘
     * 
     * LSFT_T(x) = 按住是Shift, 点击是x
     */
    [1] = LAYOUT(
        KC_F7,           KC_F8,           KC_F9,           KC_F10,          KC_NO,           KC_NO,
        LSFT_T(KC_8),    LSFT_T(KC_9),    LSFT_T(KC_0),    KC_O,            KC_F11,          KC_F12,
        LSFT_T(KC_LBRC), LSFT_T(KC_RBRC), KC_NO,           KC_L,            KC_P,            S(KC_BSLS),
        LSFT_T(KC_LBRC), KC_PGUP,         S(KC_DOT),       S(KC_COMM),      LSFT_T(KC_MINS), KC_NO,
        S(KC_SCLN),      KC_HOME,         KC_PGDN,         KC_END,          KC_PAST,         LSFT_T(KC_SLSH),
        KC_TRNS,         KC_TRNS,         KC_TRNS,         KC_TRNS,         KC_TRNS,         KC_TRNS
    ),

    [2] = LAYOUT(
        KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
        KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
        KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
        KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
        KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
        KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS
    ),

    [3] = LAYOUT(
        KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
        KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
        KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
        KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
        KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
        KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS
    )
};
