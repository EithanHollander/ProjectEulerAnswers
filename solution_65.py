from math import gcd

if __name__ == '__main__':

    def get_number_in_sequence_of_e(placement):
        # placement starts at 1
        if placement % 3 == 2:
            return int(2 * ((placement + 1) / 3))
        return 1

    e_whole_number = 2
    numerator = 1
    # They wanted the 100th convergent sum
    denominator = get_number_in_sequence_of_e(99)

    for i in range(98, 0, -1):
        whole_number = get_number_in_sequence_of_e(i)
        new_numerator = whole_number * denominator + numerator
        # Now we switch roles because it's always gonna turn into 1/(result)
        numerator = denominator
        denominator = new_numerator
        if i == 1:
            numerator += e_whole_number * denominator

    print(sum([int(c) for c in str(numerator)]))