#  Assuming digits are from 1 to some n, in a row
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def what_range_needs_to_be_checked(size_of_vector):
    return range(10 ** ((len(digits) // size_of_vector) - 1), 10 ** (len(digits) // size_of_vector))


def concatenated_product(num, vect):
    final_str = ""
    for i in vect:
        final_str += str(num * i)
    return int(final_str)


def is_number_pandigital(num):
    unique_str = ''.join(set(str(num)))
    if len(unique_str) != len(str(num)):
        return False
    for d in digits:
        if str(d) not in unique_str:
            return False
    return True


if __name__ == '__main__':

    max_pandigital = 0
    for vect_size in digits[1:]:
        vect = range(1, vect_size + 1)
        for x in what_range_needs_to_be_checked(vect_size):
            result_of_product = concatenated_product(x, vect)
            if is_number_pandigital(result_of_product) and result_of_product > max_pandigital:
                max_pandigital = result_of_product

    print(max_pandigital)
