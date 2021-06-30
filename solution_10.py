if __name__ == '__main__':
    all_nums_till = [x for x in range(2, 2_000_001)]
    is_nums_prime = [True for x in range(2, 2_000_001)]

    sum_of_primes = 0
    for i in all_nums_till:
        if is_nums_prime[i-2]:
            j = 2 * i
            while j < 2_000_001:
                is_nums_prime[j-2] = False
                j += i
            sum_of_primes += i

    print(sum_of_primes)