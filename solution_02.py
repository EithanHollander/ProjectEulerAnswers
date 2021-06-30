if __name__ == '__main__':
    first_fib_number = 1
    second_fib_number = 2
    sum_of_even_fibs = 0

    while (second_fib_number < 4_000_000):
        if (second_fib_number % 2) == 0:
            sum_of_even_fibs += second_fib_number
        temp_fib = first_fib_number
        first_fib_number = second_fib_number
        second_fib_number = temp_fib + first_fib_number

    print(sum_of_even_fibs)