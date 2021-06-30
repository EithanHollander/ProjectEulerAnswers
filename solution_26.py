if __name__ == '__main__':
    def find_recurring_cycle(x):
        left_history = []
        left_number = 1
        while left_number is not 0:
            mod_result = int((left_number * 10) / x)
            left_number = (left_number * 10) - x * mod_result
            if left_number in left_history:
                return(len(left_history) - left_history.index(left_number))
            else:
                left_history.append(left_number)
        return 0

    max_size_of_cycle = 0
    number_with_biggest_cycle = 0
    for i in range(1, 1001):
        current_size_of_cycle = find_recurring_cycle(i)
        if current_size_of_cycle > max_size_of_cycle:
            max_size_of_cycle = current_size_of_cycle
            number_with_biggest_cycle = i
    print(number_with_biggest_cycle)
