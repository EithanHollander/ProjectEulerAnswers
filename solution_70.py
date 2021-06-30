from math import sqrt

from solution_3 import check_if_prime
from solution_69 import get_primes


def get_prime_divisors(n):
    divisors = []
    for x in get_primes(2, int(n/2)):
        if n % x == 0:
            divisors.append(x)
    return divisors


def are_permutations(x, y):
    return sorted(''.join(str(x))) == sorted(''.join(str(y)))


def phi(n):
    if n == 1:
        return 1
    if check_if_prime(n):
        return n-1
    mult = 1
    for p in get_prime_divisors(n):
        mult *= (1 - 1/p)
    return int(n * mult)


# Found it on the internet - makes sense though...
# p1,p2 are the two prime divisors of n which we are trying to find its phi
def special_phi(p1, p2):
    return (p1 - 1) * (p2 - 1)


if __name__ == '__main__':
    limit = 10_000_000
    sqrt_of_limit = sqrt(limit)
    primes_list = get_primes(int(sqrt_of_limit - sqrt_of_limit / 3), int(sqrt_of_limit + sqrt_of_limit / 3))
    min_ratio = 2
    n_for_min_ratio = 0
    for p1 in primes_list:
        for p2 in primes_list:
            current_n = p1 * p2
            if current_n < limit:
                current_phi = special_phi(p1, p2)
                if are_permutations(current_n, current_phi):
                    current_ratio = current_n / current_phi
                    if min_ratio > current_ratio:
                        min_ratio = current_ratio
                        n_for_min_ratio = current_n
    print(n_for_min_ratio)