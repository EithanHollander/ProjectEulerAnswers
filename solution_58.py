from solution_3 import check_if_prime

if __name__ == '__main__':
    amount_of_primes = 0
    amount_of_numbers = 1
    number_counter = 1
    radius = 3
    while True:
        for i in range(0, 4):
            number_counter += radius - 1
            if check_if_prime(number_counter):
                amount_of_primes += 1
            amount_of_numbers += 1
        if float(amount_of_primes) / float(amount_of_numbers) < 0.1:
            break
        radius += 2
    print(radius)
    print(amount_of_primes, amount_of_numbers)