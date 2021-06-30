from solution_15 import fact

def ncr(n, r):
    if n < r:
        return 0
    fact_n = fact_r = fact_n_r = 1
    for i in range(2, n+1):
        fact_n *= i
        if i <= r:
            fact_r *= i
        if i <= n-r:
            fact_n_r *= i
    return int(fact_n / (fact_r * fact_n_r))

if __name__ == '__main__':
    amount_of_ncrs_over_million = 0
    for n in range(1, 101):
        for r in range(0, n):
            if ncr(n, r) > 1_000_000:
                amount_of_ncrs_over_million += 1
    print(amount_of_ncrs_over_million)
