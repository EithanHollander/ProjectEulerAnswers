if __name__ == '__main__':
    # Every number that's above 9 (10, 11, etc.) - will not have a product which its length equals to the exponent.
    amount = 0
    for i in range(1, 10):  # Not including 0 as a base - only Positive
        exp = 1
        while len(str(pow(i, exp))) == exp:
            amount += 1
            exp += 1
    print(amount)