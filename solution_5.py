def divided_by_1_to_20(num):
    for i in range(1, 21):
        if num % i != 0:
            return False
    return True


if __name__ == '__main__':

    num = 20
    while(True):
        if divided_by_1_to_20(num):
            print(num)
            break
        num += 20
