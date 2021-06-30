if __name__ == '__main__':
    from math import sqrt

    a = 0
    b = 0
    c = 0

    for i in range(1001):
        for j in range(i, 1001):
            k = sqrt(i*i + j*j)
            if k.is_integer():
                if i+j+k == 1000:
                    a = i
                    b = j
                    c = k
                    break

    print(a * b * c)