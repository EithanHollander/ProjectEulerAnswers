if __name__ == '__main__':

    def position_after_adding_number(starting_position, num):
        return starting_position + len(str(num))

    def new_position_and_passing_digit(starting_position, num_to_add, digit_position_to_check):
        new_position = position_after_adding_number(starting_position, num_to_add)
        temp_digit = None
        if new_position >= digit_position_to_check:
            temp_digit = int(str(num_to_add)[-(new_position - digit_position_to_check + 1)])
        return new_position, temp_digit

    def get_multiplication_of_digits_in_positions(digit_positions):
        digit_positions = sorted(digit_positions)
        position = 0
        number_to_add = 1
        current_position_to_find_counter = 0
        mult_of_found_digits = 1
        while current_position_to_find_counter < len(digit_positions):
            position, maybe_a_digit = new_position_and_passing_digit(position, number_to_add, digit_positions[current_position_to_find_counter])
            if maybe_a_digit:
                mult_of_found_digits *= maybe_a_digit
                current_position_to_find_counter += 1
            number_to_add += 1
        return mult_of_found_digits


    print(get_multiplication_of_digits_in_positions([1, 10, 100, 1000, 10000, 100000, 1000000]))
