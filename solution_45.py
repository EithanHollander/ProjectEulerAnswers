import math
from solution_44 import is_pentagonal_number

# def is_hexagonal_number(number):
#     return (math.sqrt(8*number + 1) + 1) % 4 == 0


def hexagonal_number(place):
    return place * (2 * place - 1)

if __name__ == '__main__':
    # Every hexagonal number is also a triangle number, therefore there's no need to check if the number is triangle.
    did_we_find_40755 = False
    i = 1
    while True:
        hexagonal_i = hexagonal_number(i)
        if is_pentagonal_number(hexagonal_i):
            print(hexagonal_i)
            if did_we_find_40755:
                break
            if hexagonal_i == 40755:
                did_we_find_40755 = True
        i += 1
