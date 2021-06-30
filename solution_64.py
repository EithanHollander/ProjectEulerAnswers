from math import sqrt

if __name__ == '__main__':

    def return_period_of_sequence(num):
        denominator_sub = original_denominator_sub = int(sqrt(num))
        numerator = original_numerator = 1
        whole_numbers_list = []
        while True:
            x = numerator / (sqrt(num) - denominator_sub)  # Will always be bigger than 1
            whole_number = int(x)
            numerator = (num - denominator_sub ** 2) / numerator
            denominator_sub = - (denominator_sub - whole_number * numerator)
            whole_numbers_list.append(whole_number)
            if numerator == original_numerator and denominator_sub == original_denominator_sub:
                break

        return len(whole_numbers_list)


    squared_number = 1
    counter = 1
    odd_periods_counter = 0
    while counter <= 10_000:
        if counter == squared_number ** 2:
            squared_number += 1
        else:
            odd_periods_counter += return_period_of_sequence(counter) % 2
        counter += 1
    print(odd_periods_counter)