from solution_15 import fact


def how_many_at_which_place(place, max_amount):
    #  For the first place which is 0, and max_amount=10, the amount will be 362880 = fact(max_amount)/max_amount
    #  Max of place is (max_amount - 1)
    return int(fact(max_amount-place)/(max_amount-place))


def get_the_permutation_in_place_of(x, all_digits):
    perm = ""
    copy_of_all_digits = [x for x in all_digits]
    amount = len(copy_of_all_digits)
    for i in range(0, amount):
        curr_place = how_many_at_which_place(i, amount)
        perm += str(copy_of_all_digits[int(x/curr_place)])
        copy_of_all_digits.remove(copy_of_all_digits[int(x/curr_place)])
        x = x % curr_place
    return perm


def get_all_permutations(all_digits):
    return [get_the_permutation_in_place_of(i, all_digits) for i in range(0, fact(len(all_digits)))]


if __name__ == '__main__':
    print(get_the_permutation_in_place_of(999_999, ["0","1","2","3","4","5","6","7","8","9"]))
