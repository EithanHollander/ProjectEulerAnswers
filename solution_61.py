from solution_24 import get_all_permutations
from solution_60 import common_list


def get_polygonal_number_formula_result(dimension, n):
    if dimension == 3:
        return int(n * (n + 1) / 2)
    if dimension == 4:
        return int(n * n)
    if dimension == 5:
        return int(n * (3 * n - 1) / 2)
    if dimension == 6:
        return int(n * (2 * n - 1))
    if dimension == 7:
        return int(n * (5 * n - 3) / 2)
    if dimension == 8:
        return int(n * (3 * n - 2))
    return 0


if __name__ == '__main__':

    def get_all_polygonal_number_with_four_digits(dimension):
        n = 1
        tris = []
        while True:
            tri = get_polygonal_number_formula_result(dimension, n)
            if tri > 9999:
                break
            if tri >= 1000:
                tris.append(tri)
            n += 1
        return tris

    def check_if_legit_and_return_range(n):
        # Already assuming n is a 4-digit number
        last_2_digits = n % 100
        if last_2_digits < 10:
            return []
        else:
            return [_ for _ in range(last_2_digits * 100, (last_2_digits + 1) * 100 - 1)]

    for perm in get_all_permutations(["3", "4", "5", "6", "7", "8"]):
        for a in get_all_polygonal_number_with_four_digits(int(perm[0])):
            for b in common_list(get_all_polygonal_number_with_four_digits(int(perm[1])), check_if_legit_and_return_range(a)):
                for c in common_list(get_all_polygonal_number_with_four_digits(int(perm[2])), check_if_legit_and_return_range(b)):
                    for d in common_list(get_all_polygonal_number_with_four_digits(int(perm[3])), check_if_legit_and_return_range(c)):
                        for e in common_list(get_all_polygonal_number_with_four_digits(int(perm[4])), check_if_legit_and_return_range(d)):
                            for f in common_list(get_all_polygonal_number_with_four_digits(int(perm[5])), check_if_legit_and_return_range(e)):
                                if f % 100 == int(a / 100):
                                    print(perm)
                                    print(a, b, c, d, e, f)
                                    print(a+b+c+d+e+f)
                                    exit()