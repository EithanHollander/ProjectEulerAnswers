import math


def check_if_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    dest_num = 600851475143
    all_factors = []
    for i in range(1, int(math.sqrt(dest_num))):
        if dest_num % i == 0:
            all_factors.append(i)

    for i in reversed(all_factors):
        if check_if_prime(i):
            print(i)
            break
