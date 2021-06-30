if __name__ == '__main__':
    first_number = 1
    second_number = 1
    next_number = 0
    fibonacci_place = 2

    while len(str(next_number)) < 1000:
        next_number = first_number + second_number
        fibonacci_place += 1
        first_number = second_number
        second_number = next_number

    print(fibonacci_place)
