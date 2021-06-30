if __name__ == '__main__':
    def sum_of_corners(width):
        return 4*width*width - 3*2*(width-1)

    total_sum = 1
    for i in range(3, 1002, 2):
        total_sum += sum_of_corners(i)
    print(total_sum)