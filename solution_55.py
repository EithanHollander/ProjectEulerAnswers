from solution_4 import is_palindrome

def add_reverse_of_number(num):
    return num + int(str(num)[::-1])

def is_lychrel_number(num):
    amount_of_tries = 0
    try_num = num
    while amount_of_tries < 50:
        try_num = add_reverse_of_number(try_num)
        if is_palindrome(try_num):
            return False
        amount_of_tries += 1

    return True

if __name__ == '__main__':
    amount_of_lychrel_numbers_below_10000 = 0
    for x in range(1, 10_000):
        if is_lychrel_number(x):
            amount_of_lychrel_numbers_below_10000 += 1
    print(amount_of_lychrel_numbers_below_10000)