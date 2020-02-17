from math import modf
from decimal import Decimal
import string


# store all the digits to be used, up to hexatridecimal (base32).
# stored as a list, the index of the digit used in the array is the value in decimal
HEXATRI_LIST = string.digits + string.ascii_letters + string.punctuation
# create a dictionary that stores all the digits and their values,
# much faster than repeated iteration through a list, inspiration from Kevin Meyers
VAL_DICT = {digit: val for val, digit in enumerate(HEXATRI_LIST)}


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 94, 'base is out of range: {}'.format(base)
    frac = False
    neg = False
    frac_num = 0

    if digits[0] == '-':
        neg = True
        digits = digits[1:]

    if '.' in digits:
        # handles the fractional function of the decode function
        frac = True
        fraction = digits[digits.find('.'):]
        digits = digits[:digits.find('.')]
        for i, digit in enumerate(fraction):
            if i != 0:
                frac_num += VAL_DICT[digit] * (base ** -i)


    dec_num = 0

    for i, digit in enumerate(reversed(digits)):
        dec_num += VAL_DICT[digit] * (base ** i)

    if neg:
        dec_num = -dec_num
    if frac:
        dec_num += frac_num
    
    return dec_num

def neg_bin_decode(digits):
    neg = False
    if digits[0] == 1:
        neg = True
    dec_num = decode(digits[1:], 2)

    if neg:
        return -dec_num
    return dec_num

def neg_bin_encode(number, bits=32):
    neg = False
    if number < 0:
        neg = True
        number = -number
    bin_num = encode(number, 2)
    len_of_bin = len(bin_num)
    if bits - len_of_bin <= 0:
        return 'you must either increase the amount of bits, or choose a smaller number to encode'
    if neg:
        return '1' + ('0'*(bits-len_of_bin - 1)) + bin_num
    return f"{'0'*(bits-len_of_bin) + bin_num} in {bits} bits, using ones compliment"



def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 1 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    # assert number >= 0, 'number is negative: {}'.format(number)

    neg = False
    frac = False
    if number < 0:
        neg = True
        number = -number


    if isinstance(number, float):
        # handles the fractional ascpect of the encode function
        frac = True
        dec_i = str(number).find('.')
        decimal = float(str(number)[dec_i:])
        dec_str = '.'
        number = int(str(number)[:dec_i])
        while decimal != 0.0:
            rem, whole_num = modf(decimal*base)
            decimal = rem
            dec_str += HEXATRI_LIST[int(whole_num)]


    num_str = ''

    # handles Unary
    if base == 1:
        num_str = '1' * number
        return num_str

    # while loop: check while the number does not equal 0
    while number != 0:
        # using python math module modf store the decimal, and the whole number from the original
        # number divided by the base. i.e. 19.8  dec = .8, whole = 19
        # dec, whole = modf(number/base)

        whole, dec = divmod(int(number), base)
        # reasign the number variable
        number = whole
        # prepend the appropriate digit into a string of the numbers
        num_str = HEXATRI_LIST[dec] + num_str

    # return the number in the corresponding base
    if neg:
        num_str = '-' + num_str
    if frac:
        num_str = num_str + dec_str
    return num_str

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    # check if the given number is base 10,
    # if it is, encode the number to the requested base
    # else, decode the number into base 10 then encode into the requested base
    if base1 == 10:
        return encode(int(digits), base2)

    dec_digits = decode(digits, base1)
    return str(encode(int(dec_digits), base2))

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')

if __name__ == '__main__':
    main()
    # print(encode(5, 1))
    # dec, whole = modf(42.42)
    # print(dec, whole)
    # print(42.42 - int(42.42) )
    # print(1.42 - 1)

    # print(round(Decimal(.42) % 1, 2))
    # print(encode(42.42, 2))
    # print(encode(15.8787, 16))
    # print(decode('1010.1101', 2))
    # print(encode(decode('1010.1101', 2), 2))

    # n = str(.542)
    # print(n[2:])
    # print(int(n[2:]))
    # print(neg_bin_encode(10, 8))
    print(decode("100000", 94))
