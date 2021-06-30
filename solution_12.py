from math import sqrt


def get_triangle_number(n):
    return sum([x for x in range(1, n+1)])


def get_amount_of_divisors(n):
    return 2 * sum([n % x == 0 for x in range(1, int(sqrt(n)))])


if __name__ == '__main__':

    i = 1
    tri = 1
    while(True):
        div = get_amount_of_divisors(tri)
        if div > 500:
            print(tri)
            break
        i += 1
        tri += i
