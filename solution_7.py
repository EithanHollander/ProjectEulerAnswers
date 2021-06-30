from solution_3 import check_if_prime


if __name__ == '__main__':

    how_many_primes = 0
    i = 2
    while True:
        if check_if_prime(i):
            how_many_primes += 1
            if how_many_primes == 10001:
                print(i)
                break
        i += 1
