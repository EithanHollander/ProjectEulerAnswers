import math


def is_pentagonal_number(number):
    return (math.sqrt(24*number + 1) + 1) % 6 == 0


def difference_between_pentagonal_numbers(position_j, position_k):
    sum_of_consecutive_differences = 0
    current_difference = 3*position_j + 1
    for i in range(position_j+1, position_k+1):
        sum_of_consecutive_differences += current_difference
        current_difference += 3
    return sum_of_consecutive_differences


def sum_of_pentagonal_numbers(position_j, position_k):
    return int((position_j * (3*position_j - 1))/2 + (position_k * (3*position_k - 1))/2)

if __name__ == '__main__':
    end = 2
    found_two_pentagonal_numbers = False
    while not found_two_pentagonal_numbers:
        for start in range(end-1, 0, -1):
            print(start, end)
            sum = sum_of_pentagonal_numbers(start, end)
            diff = difference_between_pentagonal_numbers(start, end)
            if is_pentagonal_number(sum) and is_pentagonal_number(diff):
                print(start, end, diff, sum)  # The answer is the diff
                found_two_pentagonal_numbers = True
                break
        end += 1

    # Another solution I found that looks good in my opinion:
    # for n in range(5000, 1, -1):
    #     for m in range(1, n):
    #         r = (1 + math.sqrt(36 * (n ** 2 + m ** 2) - 12 * (m + n) + 1)) / 6
    #         q = (1 + math.sqrt(36 * (n ** 2 - m ** 2) + 12 * (m - n) + 1)) / 6
    #         if r.is_integer() and q.is_integer():
    #             print("D is", (q * (3 * q - 1)) / 2, "its the", q,
    #                   "th term on the list and its the difference bewtween", n, "th term and", m, "th term")

