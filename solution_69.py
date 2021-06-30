from solution_3 import check_if_prime


def get_primes(start, end):
    pl = []
    for i in range(start, end+1):
        if check_if_prime(i):
            pl.append(i)
    return pl


if __name__ == '__main__':
    # Have taken some help from the internet..
    # Didn't come up to mind that the number with the most prime divisors under a million will be the one we're looking for
    # It's correct because if you have more divisors, your phi will get lower and ratio will get higher
    # So we're getting the biggest number with the most divisors
    result = 1
    primes = get_primes(2, 200)
    i = 0
    limit = 1000000
    while result * primes[i] < limit:
        result *= primes[i]
        i += 1
    print(result)