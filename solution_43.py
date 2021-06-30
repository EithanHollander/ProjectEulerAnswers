from solution_15 import fact
from solution_24 import get_the_permutation_in_place_of


first_seven_primes = [2, 3, 5, 7, 11, 13, 17]

if __name__ == '__main__':
    def first_three_digits_as_number(number, starting_position):
        # starting position starts at 0
        return int(str(number)[starting_position:starting_position+3])

    sum_of_numbers_with_the_property = 0
    for perm in range(0, fact(10)):
        current_pandigital_number_as_string = get_the_permutation_in_place_of(perm, ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        # optimization - divided by 5
        if current_pandigital_number_as_string[5] != "5":
            continue
        current_pandigital_has_substring_divisibility_property = True
        for pos in range(2, 9):
            if first_three_digits_as_number(current_pandigital_number_as_string, pos - 1) % first_seven_primes[pos-2] != 0:
                current_pandigital_has_substring_divisibility_property = False
                break
        if current_pandigital_has_substring_divisibility_property:
            sum_of_numbers_with_the_property += int(current_pandigital_number_as_string)

    print(sum_of_numbers_with_the_property)