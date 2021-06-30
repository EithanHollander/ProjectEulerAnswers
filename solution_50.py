from solution_3 import check_if_prime

if __name__ == '__main__':
    prime_with_the_longest_sum = 0
    length_of_longest_sum = 0
    primes_list = [2]
    sums_for_first_prime = [2]
    last_sum_got_over_needed = False
    for i in range(3, 1_000_000+1, 2):
        if last_sum_got_over_needed:
            break
        if check_if_prime(i):
            primes_list.append(i)
            new_sum = sums_for_first_prime[-1] + i
            sums_for_first_prime.append(new_sum)
            diffs_to_check = [0] + primes_list
            diff_sum = sums_for_first_prime[-1]
            if diff_sum > 1_000_000:
                last_sum_got_over_needed = True
            for prime_we_already_found in diffs_to_check:
                diff_sum = diff_sum - prime_we_already_found
                if check_if_prime(diff_sum) and len(primes_list) - diffs_to_check.index(prime_we_already_found) > length_of_longest_sum:
                    length_of_longest_sum = len(primes_list) - diffs_to_check.index(prime_we_already_found)
                    prime_with_the_longest_sum = diff_sum

    print(prime_with_the_longest_sum)
    print(length_of_longest_sum)

