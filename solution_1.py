if __name__ == '__main__':
    sum_of_3_5_mults = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_3_5_mults += i
    print(sum_of_3_5_mults)