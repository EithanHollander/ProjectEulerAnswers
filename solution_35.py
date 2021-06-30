import math
from solution_3 import check_if_prime


if __name__ == '__main__':
    def list_of_rotations(str):
        lst = []
        for place in range(len(str), -1, -1):
            lst.append(str[place:] + str[:place])
        return lst


    impossible_digits_for_a_circular_number = ["0", "2", "4", "6", "8", "5"]
    circular_numbers = [True for _ in range(1, 1_000_000)]
    #  Any number above 5 with the digit 2,4,5,6,8,0 will not be circular numbers
    for x in range(1, 1_000_000):
        for d in str(x):
            if d in impossible_digits_for_a_circular_number:
                circular_numbers[x-1] = False

    #  2,3,5 are the only circular numbers that contain the impossible digits
    circular_numbers[1] = circular_numbers[2] = circular_numbers[4] = True
    circular_numbers[0] = False

    for num in range(7, 1_000_000):
        if circular_numbers[num - 1] is True:
            lor = list_of_rotations(str(num))
            for rot in lor:
                if not check_if_prime(int(rot)):
                    for rot2 in lor:
                        circular_numbers[int(rot2) - 1] = False
                    break

    print(sum(circular_numbers))
