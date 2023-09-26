# Jeff's Modifier Dictionary
import re

# Trigger ending: -TZ
#
# * `F`: Control
# * `R`: Shift
# * `P`: Super
# * `B`: Alt
#
# Mode selected by AOL keys
# L not pressed:  Fingerspelling
# `L` pressed:  Navigation layer
# `UL` pressed:  Keys layer
# `EUL` pressed: Numbers layer

LONGEST_KEY = 1

STROKE_MAP = {
    # Fingerspelling.
    "A": "a",
    "PW": "b",
    "KR": "c",
    "TK": "d",
    "E": "e",
    "TP": "f",
    "TKPW": "g",
    "H": "h",
    "EU": "i",
    "SKWR": "j",
    "K": "k",
    "HR": "l",
    "PH": "m",
    "TPH": "n",
    "O": "o",
    "P": "p",
    "KW": "q",
    "R": "r",
    "S": "s",
    "T": "t",
    "U": "u",
    "SR": "v",
    "W": "w",
    "KP": "x",
    "KWR": "y",
    "STKPW": "z",

    # Navigation layer
    "PL": "up",
    "KL": "left",
    "WL": "down",
    "RL": "right",
    "TPHL": "page_up",
    "KWRL": "page_down",
    "TKL": "home",
    "HRL": "end",
    "TL": "backspace",
    "HL": "delete",

    # Keys layer
    "TKUL": "escape",
    "HRUL": "tab",
    "HUL": "quoteright",
    "WRUL": "space",
    "WHRUL": "return",
    "KPUL": "slash",
    "TWUL": "backslash",
    "PHUL": "minus",
    "TKPWUL": "equal",
    "KUL": "period",
    "WUL": "comma",
    "KWUL": "semicolon",
    "PUL": " quoteleft",
    "TPHUL": "braceleft",
    "KWRUL": "braceright",

    # Number layer
    "EUL": "0",
    "REUL": "1",
    "WEUL": "2",
    "WREUL": "3",
    "KEUL": "4",
    "KREUL": "5",
    "KWEUL": "6",
    "KWREUL": "7",
    "SEUL": "8",
    "SREUL": "9",

    "PEUL": "KP_0",
    "PREUL": "KP_1",
    "PWEUL": "KP_2",
    "PWREUL": "KP_3",
    "KPEUL": "KP_4",
    "KPREUL": "KP_5",
    "KPWEUL": "KP_6",
    "KPWREUL": "KP_7",
    "SPEUL": "KP_8",
    "SPREUL": "KP_9",

    "TPREUL": "F1",
    "TPWEUL": "F2",
    "TPWREUL": "F3",
    "TKPEUL": "F4",
    "TKPREUL": "F5",
    "TKPWEUL": "F6",
    "TKPWREUL": "F7",
    "STPEUL": "F8",
    "STPREUL": "F9",
    "STPWEUL": "F10",
    "STPWREUL": "F11",
    "STKPEUL": "F12",
    "STKPREUL": "F13",
    "STKPWEUL": "F14",
    "STKPWREUL": "F15",
}

PARTS_MATCHER = re.compile(
    r'(S?T?K?P?W?H?R?)(A?O?)([-*]?)(E?U?)(F?R?P?B?)(L?)TZ'
)


def lookup(chord):
    if len(chord) != 1:
        raise KeyError

    stroke = chord[0]
    match = PARTS_MATCHER.fullmatch(stroke)
    if not match:
        raise KeyError

    (keys, vowels1, separator, vowels2, modifiers, layer) = match.groups()
    pattern = keys + vowels1 + vowels2 + layer

    result = STROKE_MAP.get(pattern)
    if not result:
        return ' '

    if "F" in modifiers:
        result = "control(%s)" % result
    if "R" in modifiers:
        result = "shift(%s)" % result
    if "P" in modifiers:
        result = "super(%s)" % result
    if "B" in modifiers:
        result = "alt(%s)" % result

    return "{#%s}" % result
