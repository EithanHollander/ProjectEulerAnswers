import math
from solution_3 import check_if_prime


if __name__ == '__main__':
    list_of_primes = []
    amount_of_consecutive_number_with_four_distinct_prime_factors = 0
    i = 2
    while True:
        if check_if_prime(i):
            list_of_primes.append(i)
            amount_of_consecutive_number_with_four_distinct_prime_factors = 0
        else:  # a prime number obviously only has one prime factor, so no need to check it
            amount_of_factors = 0
            for x in list_of_primes:
                if x > i / 2:
                    break
                if i % x == 0:
                    amount_of_factors += 1
            print(i, amount_of_factors)
            if amount_of_factors == 4:
                amount_of_consecutive_number_with_four_distinct_prime_factors += 1
            else:
                amount_of_consecutive_number_with_four_distinct_prime_factors = 0
        if amount_of_consecutive_number_with_four_distinct_prime_factors == 4:
            print(i-3, i-2, i-1, i)
            break
        i += 1