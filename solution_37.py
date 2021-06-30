import math
from solution_3 import check_if_prime

if __name__ == '__main__':

    def is_truncatable_left_to_right(num):
        tmp_num = num
        while tmp_num > 0:
            if not check_if_prime(tmp_num):
                return False
            tmp_num %= 10 ** (len(str(tmp_num)) - 1)
        return True

    def is_truncatable_right_to_left(num):
        tmp_num = num
        while tmp_num > 0:
            if not check_if_prime(tmp_num):
                return False
            tmp_num //= 10
        return True


    how_many_truncatable_we_found = 0
    sum_of_truncatables = 0
    i = 10
    while how_many_truncatable_we_found < 11:
        if is_truncatable_left_to_right(i) and is_truncatable_right_to_left(i):
            print(i)
            how_many_truncatable_we_found += 1
            sum_of_truncatables += i
        i += 1

    print(sum_of_truncatables)
