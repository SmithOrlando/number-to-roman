'''
    the program consist of taking a decimal number
    as an input and ouput a roman of that input
    number.

    Decimal             Roman
    1                   I
    4                   IV
    5                   V
    9                   IX
    10                  X
    40                  XL
    50                  L
    90                  XC
    100                 C
    400                 CD
    500                 D
    900                 CM
    1000                M
'''


def decimal_to_roman(references, decimal, number):
    Number = number
    Reference = references.copy()
    length = len(decimal)
    romans = ""


    while Number != 0:
        for index in range(length, 0, -1):
            if decimal[index-1] <= Number :
                Number -= decimal[index-1]
                romans += Reference[decimal[index-1]]
                break


    return romans


if __name__ == '__main__':
    references = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }

    decimal = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]


    number = int(input())

    result = decimal_to_roman(references, decimal, number)

    print(result)

