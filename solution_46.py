import math
from solution_3 import check_if_prime

if __name__ == '__main__':
    found_first_composite_number_contradict_goldbach = False
    list_of_primes = []
    i = 3
    while not found_first_composite_number_contradict_goldbach:
        if check_if_prime(i):
            list_of_primes.append(i)
        else:
            found_a_sqrt = False
            for x in list_of_primes:
                y = math.sqrt((i - x) / 2)
                if y.is_integer():
                    found_a_sqrt = True
                    break
            if not found_a_sqrt:
                found_first_composite_number_contradict_goldbach = False
                print(i)
                break
        i += 2