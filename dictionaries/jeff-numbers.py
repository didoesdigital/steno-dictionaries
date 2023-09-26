# Jeff's Numbers dictionary for Plover.
#
# See README.md for usage details.
import re

LONGEST_KEY = 20
DIGITS = '0123456789'
ENDING_DIGITS_MATCHER = re.compile(r'\d+$')
ENDING_NUMBER_MATCHER = re.compile(r'.?\d[\d,.]*$')
AM_SUFFIX = ' a.m.'
PM_SUFFIX = ' p.m.'


def lookup(key):
    result = ''
    needs_space = False
    next_error = False
    use_glue = True

    for stroke in key:
        if next_error:
            raise KeyError

        if not any(c in stroke for c in DIGITS) and not '#' in stroke:
            raise KeyError

        if needs_space:
            result += ' '
            needs_space = False

        stroke_digits = digits(stroke)
        result += stroke_digits
        control = ''.join(c for c in stroke if c not in '0123456789#-EU')
        if stroke_digits.endswith(','):
            control = control.replace('*S', '')

        if 'RB' in control:
            control = control.replace('RB', '')
            if len(result) >= 1 and result[-1] == '.':
                result = result + r'0 {*($c)}'
            else:
                result = result + r' {*($c)}'
            use_glue = False
            needs_space = True
            next_error = True
        elif 'WR' in control:
            control = control.replace('WR', '')
            if len(result) >= 1 and result[-1] == '.':
                result = result + r'0 {*($c)}'
            else:
                result = result + r' {*($c)}'
            use_glue = False
            needs_space = True
            next_error = True
        elif 'KR' in control:
            control = control.replace('KR', '')
            result = ENDING_NUMBER_MATCHER.sub(r'\g<0>%', result)
            needs_space = True
            next_error = True
        elif 'RG' in control:
            control = control.replace('RG', '')
            result = ENDING_NUMBER_MATCHER.sub(r'\g<0>%', result)
            needs_space = True
            next_error = True
        elif 'DZ' in control:
            if '*' in control:
                result = result + r'000 {*($c)}'
            else:
                result = result + r'00 {*($c)}'
            needs_space = True
            next_error = True
            use_glue = False
        elif 'K' in control or 'BG' in control:
            if 'K' not in control:
                result += ':00'
            elif 'BG' in control:
                result += ':45'
            elif 'G' in control:
                result += ':15'
            elif 'B' in control:
                result += ':30'
            else:
                result += ':00'

            if 'S' in control:
                result += PM_SUFFIX if '*' in control else AM_SUFFIX

            needs_space = True
            next_error = True
            use_glue = False
            control = ''.join(c for c in control if c not in 'KBGS')
        elif 'G' in control:
            match = ENDING_NUMBER_MATCHER.search(result)
            if not match:
                raise KeyError
            words = toWords(''.join(c for c in match.group(0) if c in DIGITS))

            if 'W' in control:
                if words.endswith('ty'):
                    words = words[:-1] + 'ieth'
                elif words.endswith('one'):
                    words = words[:-3] + 'first'
                elif words.endswith('two'):
                    words = words[:-3] + 'second'
                elif words.endswith('three'):
                    words = words[:-5] + 'third'
                elif words.endswith('ve'):          # fifth and twelfth
                    words = words[:-2] + 'fth'
                elif words.endswith('eight'):
                    words += 'h'
                elif words.endswith('nine'):
                    words = words[:-1] + 'th'
                else:
                    words += 'th'

            result = match.expand(words)
            needs_space = True
            next_error = True
            use_glue = False
            control = ''.join(c for c in control if c not in 'WG')
        elif 'W' in control or 'B' in control:
            match = ENDING_DIGITS_MATCHER.search(result)
            if not match:
                raise KeyError

            needs_space = True
            next_error = True
            use_glue = False
            control = ''.join(c for c in control if c not in 'WB')

            if len(result) >= 1 and result[-1] == '1':
                result += 'th' if len(
                    result) >= 2 and result[-2] == '1' else 'st'
            elif len(result) >= 1 and result[-1] == '2':
                result += 'th' if len(
                    result) >= 2 and result[-2] == '1' else 'nd'
            elif len(result) >= 1 and result[-1] == '3':
                result += 'th' if len(
                    result) >= 2 and result[-2] == '1' else 'rd'
            else:
                result += 'th'
        elif 'R' in control:
            match = ENDING_NUMBER_MATCHER.search(result)
            if not match:
                raise KeyError

            value = int(''.join(c for c in match.group(0) if c in DIGITS))
            if value < 0 or value > 3999:
                raise KeyError

            roman = toRoman(value)

            if '*' in control:
                roman = roman.lower()
            result = match.expand(roman)

            control = control.replace('R', '')
            needs_space = True
            next_error = True
            use_glue = False

        control = ''.join(c for c in control if c not in 'DZ*')
        if control != '':
            raise KeyError

    if use_glue:
        result = "{&%s}" % result

    return result


def digits(val):
    result = ''.join(c for c in val if c in DIGITS)
    control = ''.join(c for c in val if c not in DIGITS)

    if 'E' in control or 'U' in control:
        control = ''.join(c for c in control if c not in 'EU')
        result = result[::-1]

    if not 'DZ' in control:
        if 'Z' in control:
            result += ',000' if '*' in control else '00'
            control = ''.join(c for c in control if c not in '*Z')

        if 'D' in control:
            if len(result) > 0:
                result += result[-1]
            control = control.replace('D', '')

    if control == '*S' or control == '#*S':
        result += ','
    elif '*' in control and (not any(c in 'RSZ' for c in control) or control == "*RB" or control == "WR*"):
        result += '.'

    return result


ROMAN_VALUES = [
    1000, 900, 500, 400,
    100, 90, 50, 40,
    10, 9, 5, 4,
    1
]
ROMAN_SYMBOLS = [
    'M', 'CM', 'D', 'CD',
    'C', 'XC', 'L', 'XL',
    'X', 'IX', 'V', 'IV',
    'I'
]


def toRoman(num):
    result = ''
    i = 0
    while num > 0:
        for _ in range(num // ROMAN_VALUES[i]):
            result += ROMAN_SYMBOLS[i]
            num -= ROMAN_VALUES[i]
        i += 1
    return result

# ---- Adapted from https://programsolve.com/python-to-convert-numbers-to-words-with-source-code/


ONE_DIGIT_WORDS = {
    '0': ["zero"],
    '1': ["one"],
    '2': ["two", "twen"],
    '3': ["three", "thir"],
    '4': ["four", "for"],
    '5': ["five", "fif"],
    '6': ["six"],
    '7': ["seven"],
    '8': ["eight"],
    '9': ["nine"],
}

TWO_DIGIT_WORDS = ["ten", "eleven", "twelve"]
HUNDRED = "hundred"
LARGE_SUM_WORDS = ["thousand", "million", "billion", "trillion", "quadrillion",
                   "quintillion", "sextillion", "septillion", "octillion", "nonillion"]


def toWords(n):
    if all(c == '0' for c in n):
        return ONE_DIGIT_WORDS['0'][0]

    word = []

    if len(n) % 3 != 0 and len(n) > 3:
        n = n.zfill(3 * (((len(n)-1) // 3) + 1))

    sum_list = [n[i:i + 3] for i in range(0, len(n), 3)]
    skip = False

    for i, num in enumerate(sum_list):
        if num != '000':
            skip = False

        for _ in range(len(num)):
            num = num.lstrip('0')
            if len(num) == 1:
                if len(word) > 0:
                    if HUNDRED in word[-1] or i == len(sum_list) - 1:
                        word.append("and")
                    elif word[-1] in LARGE_SUM_WORDS:
                        word[-1] = word[-1] + ','
                word.append(ONE_DIGIT_WORDS[num][0])
                num = num[1:]
                break

            if len(num) == 2:
                if num[0] != '0':
                    if len(word) > 0:
                        if HUNDRED in word[-1] or i == len(sum_list) - 1:
                            word.append("and")
                        elif word[-1] in LARGE_SUM_WORDS:
                            word[-1] = word[-1] + ','
                    if num.startswith('1'):
                        if int(num[1]) in range(3):
                            word.append(TWO_DIGIT_WORDS[int(num[1])])
                        else:
                            number = ONE_DIGIT_WORDS[num[1]][1 if int(
                                num[1]) in range(3, 6, 2) else 0]
                            word.append(
                                number + ("teen" if not number[-1] == 't' else "een"))
                    else:
                        word.append(ONE_DIGIT_WORDS[num[0]][1 if int(num[0]) in range(2, 6) else 0] + (
                            "ty" if num[0] != '8' else 'y') + ('-' + ONE_DIGIT_WORDS[num[1]][0] if num[1] != '0' else ""))
                    break
                else:
                    num = num[1:]
                    continue

            if len(num) == 3:
                if num[0] != '0':
                    if len(word) > 0:
                        word[-1] = word[-1] + ','
                    word.append(ONE_DIGIT_WORDS[num[0]][0] + " " + HUNDRED)
                    if num[1:] == '00':
                        break
                num = num[1:]

        if len(sum_list[i:]) > 1 and not skip:
            word.append(LARGE_SUM_WORDS[len(sum_list[i:]) - 2])
            skip = True

    return " ".join(map(str.strip, word))
