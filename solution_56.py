if __name__ == '__main__':
    biggest_sum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            curr_sum = sum([int(d) for d in str(a**b)])
            if curr_sum > biggest_sum:
                biggest_sum = curr_sum
    print(biggest_sum)