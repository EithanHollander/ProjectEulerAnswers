from solution_3 import check_if_prime

if __name__ == '__main__':
    x = 2
    found_an_eight_family = False
    while not found_an_eight_family:
        if check_if_prime(x):
            str_x = str(x)
            array_of_digits_exist = [(str(i) in str_x) for i in range(0, 10)]
            for digit in range(0, 10):
                if array_of_digits_exist[digit]:
                    amount_of_new_primes = 0
                    # what_digits_we_have_switched = []
                    for other_digit in [i for i in range(0, 10) if
                                        i != digit and not (i == 0 and str_x.index(str(digit)) == 0)]:
                        new_x = str_x.replace(str(digit), str(other_digit))
                        if check_if_prime(int(new_x)):
                            amount_of_new_primes += 1
                            # what_digits_we_have_switched.append(other_digit)
                    if amount_of_new_primes == 7:
                        found_an_eight_family = True
                        # print(digit)
                        # print(what_digits_we_have_switched)
                        break
        x += 1
    print(x - 1)