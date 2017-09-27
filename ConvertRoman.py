roman_dataframe = (
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1)
)

to_roman_table = [None]
from_roman_table = {}


def to_roman(n):
    """Convert integer to Roman numeral"""
    if n < 1 or n > 4999:
        print("Numbers Should be between 1 and 4999")
    return to_roman_table[n]


def from_roman(n):
    """Convert Roman numeral to integer"""
    if not n:
        print("Empty String")
    if n not in from_roman_table:
        print("Not valid Roman Numeral")
    return from_roman_table[n]

def convert_numeral():
    #Read input
    def to_roman(n):
        result = ''
        for numeral, integer in roman_dataframe:
            if n >= integer:
                result = numeral
                n -= integer
                break
        if n > 0:
            result += to_roman_table[n]
        return result
    #Transform numeral
    for integer in range(1, 5000):
        roman_numeral = to_roman(integer)
        to_roman_table.append(roman_numeral)
        from_roman_table[roman_numeral] = integer

convert_numeral()
