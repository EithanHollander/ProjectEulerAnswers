from math import gcd


def proper_fractions(d):
    fractions = []
    for counter_d in range(2, d):
        for n in range(1, counter_d):
            if gcd(n, d) == 1:
               fractions.append(n/counter_d)
    return sorted(fractions)


def closest_proper_fraction_to_3_7(d):
    if d == 2:
        return 0, 0
    if d == 7:
        return 2/7, 2
    n = int(3 * d / 7)
    while gcd(n,d) != 1:
        n -= 1
    return n/d, n


if __name__ == '__main__':
    closest_frac = 0
    closest_numerator = 0
    for d in range(2, 1_000_000):
        current_frac, current_numerator = closest_proper_fraction_to_3_7(d)
        if current_frac > closest_frac:
            closest_frac = current_frac
            closest_numerator = current_numerator
    print("************************")
    print(closest_frac, closest_numerator)