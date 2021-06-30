from solution_3 import check_if_prime
from solution_15 import fact
from solution_24 import get_the_permutation_in_place_of


if __name__ == '__main__':
    def get_largest_prime_pandigital_number():
        for amount_of_digits in range(9, 0, -1):
            array_of_digits = [i for i in range(1, amount_of_digits+1)]
            for placement in range(fact(amount_of_digits) - 1, -1, -1):
                perm = get_the_permutation_in_place_of(placement, array_of_digits)
                if check_if_prime(int(perm)):
                    return perm

    print(get_largest_prime_pandigital_number())
