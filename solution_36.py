from solution_4 import is_palindrome


def to_bin(x):
    return format(x, 'b')


if __name__ == '__main__':
    print(sum([x for x in range(1, 1_000_000, 2) if is_palindrome(x) and is_palindrome(to_bin(x))]))
