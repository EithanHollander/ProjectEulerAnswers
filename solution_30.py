if __name__ == '__main__':
    fifth_powers = [x**5 for x in range(10)]

    def find_sum_of_digits_fifth_powers(x):
        sum = 0
        for c in str(x):
            #  I used a pre-defined array to save computing time
            sum += fifth_powers[int(c)]
        return sum

    i = 2
    sum = 0
    #  9^5 = 59,049, for 2-digit number the max value is 2*9^5=118,098 for 99
    #  for 5-digit number, the max is 5*9^5=295,245 for 99,999, so there's still a chance that the sum of fifth powers of digits will be equal to the number itself
    #  when it comes to 6-digits, the max is 6*9^5=354,294 for 999,999 which is not even close, and it will keep being smaller than the original number as we add more digits
    #  therefore we don't not to check for more than 999,999 (we can find a smaller number to check until, but it's good enough)
    while i < 999_999:
        if i == find_sum_of_digits_fifth_powers(i):
            sum += i
        i += 1

    print(sum)
