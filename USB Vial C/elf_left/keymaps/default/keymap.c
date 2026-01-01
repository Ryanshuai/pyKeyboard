#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * Layer 0: Normal (左手)
     * ┌────┬────┬────┬────┬────┬────┐
     * │    │    │ 2  │ 3  │ 4  │ 5  │
     * ├────┼────┼────┼────┼────┼────┤
     * │ `  │ 1  │ W  │ E  │ R  │ T  │
     * ├────┼────┼────┼────┼────┼────┤
     * │ +  │ Q  │ S  │ D  │ F  │ G  │
     * ├────┼────┼────┼────┼────┼────┤
     * │ -  │ A  │ X  │ C  │ V  │ B  │
     * ├────┼────┼────┼────┼────┼────┤
     * │ESC │ Z  │BSPC│SPC │ENT │TAB │
     * ├────┼────┼────┼────┼────┼────┤
     * │Fn1 │Ctrl│Alt │GUI │Shft│C+F8│
     * └────┴────┴────┴────┴────┴────┘
     */
    [0] = LAYOUT(
        KC_NO,   KC_NO,   KC_2,    KC_3,    KC_4,    KC_5,
        KC_GRV,  KC_1,    KC_W,    KC_E,    KC_R,    KC_T,
        KC_PPLS, KC_Q,    KC_S,    KC_D,    KC_F,    KC_G,
        KC_PMNS, KC_A,    KC_X,    KC_C,    KC_V,    KC_B,
        KC_ESC,  KC_Z,    KC_BSPC, KC_SPC,  KC_ENT,  KC_TAB,
        MO(1),   KC_LCTL, KC_LALT, KC_LGUI, KC_LSFT, C(KC_F8)
    ),

    /* Layer 1: Fn1 */
    [1] = LAYOUT(
        KC_NO,   KC_NO,   KC_F3,      KC_F4,      KC_F5,      KC_F6,
        KC_F1,   KC_F2,   KC_W,       S(KC_COMM), S(KC_DOT),  KC_QUOT,
        KC_PPLS, KC_Q,    KC_S,       S(KC_9),    S(KC_0),    S(KC_QUOT),
        KC_PMNS, KC_A,    KC_X,       KC_LBRC,    KC_RBRC,    KC_SCLN,
        KC_ESC,  KC_Z,    KC_BSPC,    S(KC_LBRC), S(KC_RBRC), KC_SCLN,
        KC_TRNS, KC_TRNS, KC_TRNS,    KC_TRNS,    KC_TRNS,    KC_TRNS
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
