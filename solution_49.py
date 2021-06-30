from solution_3 import check_if_prime
if __name__ == '__main__':
    list_of_same_digits_terms = {}

    for x in range(1001, 10001, 2):
        if check_if_prime(x):
            sorted_num = ''.join(sorted(str(x)))
            list_of_same_digits_terms.setdefault(sorted_num, [])
            list_of_same_digits_terms[sorted_num].append(x)

    only_at_least_three_numbers_long_lists = [sorted(list_of_same_digits_terms[k]) for k in list_of_same_digits_terms.keys() if len(list_of_same_digits_terms[k]) >= 3]
    for three_plus_list in only_at_least_three_numbers_long_lists:
        for a in three_plus_list:
            for b in three_plus_list:
                for c in three_plus_list:
                    if a > b > c:
                        if a-b == b-c:
                            print(str(c) + str(b) + str(a))
                            # print(three_plus_list, c, b, a)