from solution_3 import check_if_prime

if __name__ == '__main__':
    def find_max_of_consecutive_range(a,b):
        n = 0
        while True:
            if not check_if_prime(n*n + a*n + b):
                return n
            n += 1

    max_range = 0
    mult_of_ab_of_max_range = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            curr_range = find_max_of_consecutive_range(a, b)
            if curr_range > max_range:
                max_range = curr_range
                mult_of_ab_of_max_range = a*b

    print(mult_of_ab_of_max_range)
