def is_palindrome(num):
    return str(num) == str(num)[::-1]


if __name__ == '__main__':
    largest_palindrome = 0

    for i in range(100,1000):
        for j in range(100, 1000):
            if is_palindrome(i*j) and i*j > largest_palindrome:
                largest_palindrome = i*j

    print(largest_palindrome)
