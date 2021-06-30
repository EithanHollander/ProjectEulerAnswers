from math import sqrt


def sum_of_divisors(n):
    sum = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            if i == n/i or i == 1:
                sum += i
            else:
                sum += i + int(n/i)
    return sum


if __name__ == '__main__':
    numbers_who_may_be_amicable = [0 for _ in range(10_000)]
    sum_of_amicables = 0
    for i in range(10_000):
        numbers_who_may_be_amicable[i] = sod = sum_of_divisors(i+1)
        if sod <= 10_000 and numbers_who_may_be_amicable[sod - 1] == i + 1 and sod != i+1:
            sum_of_amicables += sod + i+1
    print(sum_of_amicables)
