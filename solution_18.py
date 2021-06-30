if __name__ == '__main__':

    # Added History of path so I could know what was the path to the final number
    triangle_of_15_levels = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
    ]

    potential_of_15_triangle = [[0 for j in range(i+1)] for i in range(15)]
    direction_of_potential_history = [["none" for j in range(i+1)] for i in range(15)]

    def get_bigger_potential_of_fathers(row, place):
        if row == 0:
            return 0
        if place == 0:
            direction_of_potential_history[row][place] = direction_of_potential_history[row-1][place] + " left"
            return potential_of_15_triangle[row-1][place]
        if place == row:
            direction_of_potential_history[row][place] = direction_of_potential_history[row-1][place-1] + " right"
            return potential_of_15_triangle[row-1][place-1]

        if potential_of_15_triangle[row-1][place-1] > potential_of_15_triangle[row-1][place]:
            direction_of_potential_history[row][place] = direction_of_potential_history[row-1][place-1] + " right"
            return potential_of_15_triangle[row-1][place-1]
        else:
            direction_of_potential_history[row][place] = direction_of_potential_history[row-1][place] + " left"
            return potential_of_15_triangle[row-1][place]

    def get_potential_of_current(row, place):
        return get_bigger_potential_of_fathers(row, place) + triangle_of_15_levels[row][place]

    for i in range(15):
        for j in range(i+1):
            potential_of_15_triangle[i][j] = get_potential_of_current(i ,j)

    index_of_biggest_potential = potential_of_15_triangle[14].index(max(potential_of_15_triangle[14]))
    print(potential_of_15_triangle[14][index_of_biggest_potential])
    print(direction_of_potential_history[14][index_of_biggest_potential])
