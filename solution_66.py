from math import sqrt


def is_perfect_square(x):
    root = sqrt(x)
    if int(root + 0.5) ** 2 == x:
        return True
    return False


def get_continued_fraction(num):
    denominator_sub = original_denominator_sub = original_whole_number = int(sqrt(num))
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

    return original_whole_number, whole_numbers_list


def get_convergent(num, placement_of_convergent):
    # Placement of convergent starts at 0
    whole, continued_fraction_list = get_continued_fraction(num)
    if placement_of_convergent == 0:
        return num, 1
    numerator = 1
    length = len(continued_fraction_list)
    denominator = continued_fraction_list[(placement_of_convergent - 1) % length]  # List starts at 0 but now the placement is at least 1
    for i in range(placement_of_convergent - 2, -1, -1):
        whole_n = continued_fraction_list[i % length]
        new_numerator = whole_n * denominator + numerator
        # Now we switch roles because it's always gonna turn into 1/(result)
        numerator = denominator
        denominator = new_numerator

    numerator += whole * denominator
    return numerator, denominator


if __name__ == '__main__':
    # Let's remember the equation if in the form of x^2 - D*y^2 = 1
    counter_D = squared_number = 1
    biggest_x = 0
    d_for_biggest_x = 0
    while counter_D <= 1000:
        if counter_D == squared_number ** 2:
            squared_number += 1
        else:
            counter_i = 1
            while True:
                possible_x, possible_y = get_convergent(counter_D, counter_i)
                if possible_x ** 2 - counter_D * possible_y ** 2 == 1:
                    if possible_x > biggest_x:
                        biggest_x = possible_x
                        d_for_biggest_x = counter_D
                    break
                counter_i += 1
        counter_D += 1

    print(d_for_biggest_x, biggest_x)