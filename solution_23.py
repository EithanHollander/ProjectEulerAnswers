from math import sqrt
from solution_21 import sum_of_divisors

# Redundant numbers must be even, since dividable odd numbers are either prime=not abdundant,
# or some mult of a prime=not enough to become redundant.

if __name__ == '__main__':

    MAX_NUMBER = 28124

    all_the_abundants = []  # Starts with no numbers in it but grows
    is_it_a_sum_of_two_abundants = [False for _ in range(1, MAX_NUMBER)]  # For x, it's place in the array will be x-1

    for x in range(12, MAX_NUMBER):
        if sum_of_dividors(x) > x:
            all_the_abundants.append(x)

    for x in range(0, all_the_abundants.__len__()):
        for y in range(0, all_the_abundants.__len__()):
            abdx = all_the_abundants[x]
            abdy = all_the_abundants[y]
            if abdx + abdy < MAX_NUMBER:
                is_it_a_sum_of_two_abundants[abdx+abdy-1] = True
            else:
                break

    sum = 0
    for x in range(0, MAX_NUMBER-1):
        if not is_it_a_sum_of_two_abundants[x]:
            sum += x+1

    print(sum)
