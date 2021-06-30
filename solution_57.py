from fractions import Fraction

if __name__ == '__main__':
    previous_denominator, current_denominator, previous_numerator, current_numerator = 1, 2, 1, 3
    temp_denominator, temp_numerator = 0, 0
    counter_of_expansions = 0
    amount_of_exceeding = 0
    while counter_of_expansions < 1000:
        if len(str(current_numerator)) > len(str(current_denominator)):
            amount_of_exceeding += 1
        counter_of_expansions += 1

        # Taking care of denominator
        temp_denominator = current_denominator
        current_denominator = 2 * current_denominator + previous_denominator
        previous_denominator = temp_denominator

        # Taking care of numerator
        temp_numerator = current_numerator
        current_numerator = 2 * current_numerator + previous_numerator
        previous_numerator = temp_numerator
    print(amount_of_exceeding)