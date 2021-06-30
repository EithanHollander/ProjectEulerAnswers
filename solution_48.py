if __name__ == '__main__':
    sum = 0
    for i in range(1, 1001):
        sum += i**i
    strsum = str(sum)
    print(strsum[len(strsum)-10:])