from solution_3 import check_if_prime


def check_sublist(big_list, small_list):
    return all([(x in big_list) for x in small_list])


def common_list(list1, list2):
    return [x for x in list1 if (x in list2)]


if __name__ == '__main__':
    def check_if_couple(prime_a, prime_b):
        return check_if_prime(int(str(prime_a) + str(prime_b))) and check_if_prime(int(str(prime_b) + str(prime_a)))

    def check_if_set(set_of_prime_numbers):
        for x in set_of_prime_numbers:
            for y in set_of_prime_numbers:
                if x == y:
                    break
                if not check_if_couple(x, y):
                    return False
        return True

    def check_if_can_add_to_exisiting_set(existing_set, wannabe_added):
        return all([check_if_couple(x, wannabe_added) for x in existing_set])

    def get_all_options_amount_of_5(list_of_values):
        if len(list_of_values) < 5:
            return None
        options = []
        for a in range(0, len(list_of_values)):
            for b in range(a+1, len(list_of_values)):
                for c in range(b+1, len(list_of_values)):
                    for d in range(c+1, len(list_of_values)):
                        for e in range(d+1, len(list_of_values)):
                            options.append([list_of_values[a], list_of_values[b], list_of_values[c], list_of_values[d], list_of_values[e]])
        return options

    primes_list = []
    pair_matches_for_primes = {}
    trios_matches_for_primes = {}
    pairs_primes = []
    trios_primes = []
    quartets_primes = []
    quintets_primes = []
    prime_counter = 3
    # Just put a random legit number to be the limit
    while prime_counter <= 32768:
        print_flag = False
        if check_if_prime(prime_counter):

            pair_matches_for_primes.setdefault(str(prime_counter), [p for p in primes_list if check_if_couple(p, prime_counter)])
            trios_matches_for_primes.setdefault(str(prime_counter), [])

            for quartet in quartets_primes:
                if check_if_can_add_to_exisiting_set(quartet, prime_counter):
                    quintets_primes.append(quartet + [prime_counter])
                    print("5:" + str(quartet + [prime_counter]) + str(sum(quartet + [prime_counter])))

            for k in trios_matches_for_primes:
                if check_if_couple(k, prime_counter):
                    for l in trios_matches_for_primes[k]:
                        if check_if_can_add_to_exisiting_set(l + [int(k)], prime_counter):
                            quartets_primes.append(l + [int(k)] + [prime_counter])
                            print("4:" + str(quartets_primes[-1]))

            for k in pair_matches_for_primes[str(prime_counter)]:
                for l in pair_matches_for_primes[str(k)]:
                    if check_if_can_add_to_exisiting_set([int(l)] + [int(k)], prime_counter):
                        trios_matches_for_primes[str(prime_counter)].append([int(l)] + [int(k)])

            primes_list.append(prime_counter)

        prime_counter += 2

    quintets_primes.sort(key=lambda x: sum(x))
    print("Smallest Primes Set:", quintets_primes[0], "Sum:", sum(quintets_primes[0]))

    # A Solution I found on the internet and I liked
    # MAX_VALUE = 32768
    # min_set_sum = MAX_VALUE
    # current_found_set = []
    # primes_list = [p for p in range(3, MAX_VALUE) if check_if_prime(p)]
    # pairing_for_primes = {}
    # for a in primes_list:
    #     if a*5 >= MAX_VALUE: break
    #     pairing_for_primes.setdefault(str(a), [p for p in primes_list[primes_list.index(a) + 1:] if check_if_couple(a, p)])
    #     for b in primes_list[primes_list.index(a)+1:]:
    #         if a + b*4 >= MAX_VALUE:
    #             break
    #         if not (b in pairing_for_primes[str(a)]):
    #             continue
    #         pairing_for_primes.setdefault(str(b),[p for p in primes_list[primes_list.index(b) + 1:] if check_if_couple(b, p)])
    #         for c in primes_list[primes_list.index(b) + 1:]:
    #             if a + b + c*3 >= MAX_VALUE:
    #                 break
    #             if not (c in pairing_for_primes[str(a)] and c in pairing_for_primes[str(b)]):
    #                 continue
    #             pairing_for_primes.setdefault(str(c), [p for p in primes_list[primes_list.index(c) + 1:] if check_if_couple(c, p)])
    #             for d in primes_list[primes_list.index(c) + 1:]:
    #                 if a + b + c + d*2 >= MAX_VALUE:
    #                     break
    #                 if not (d in pairing_for_primes[str(a)] and d in pairing_for_primes[str(b)] and d in pairing_for_primes[str(c)]):
    #                     continue
    #                 print(a, b, c, d)
    #                 pairing_for_primes.setdefault(str(d), [p for p in primes_list[primes_list.index(d) + 1:] if check_if_couple(d, p)])
    #                 for e in primes_list[primes_list.index(d) + 1:]:
    #                     if a + b + c + d + e >= MAX_VALUE:
    #                         break
    #                     if not (e in pairing_for_primes[str(a)] and e in pairing_for_primes[str(b)] and e in pairing_for_primes[str(c)] and e in pairing_for_primes[str(d)]):
    #                         continue
    #
    #                     if a + b + c + d + e < min_set_sum:
    #                         current_found_set = [a, b, c, d, e]
    #                         min_set_sum = a + b + c + d + e
    #                         print(current_found_set, min_set_sum)
    #                         break
