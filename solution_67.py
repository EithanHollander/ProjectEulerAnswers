if __name__ == '__main__':
    # Pretty much taking the code from solution 18 :D

    triangle_of_100_levels = []
    with open("problem_67_triangle.txt") as read_triangle:
        for line in read_triangle.readlines():
            triangle_of_100_levels.append([int(x) for x in line.split()])

    # Added History of path so I could know what was the path to the final number

    potential_of_100_triangle = [[0 for j in range(i + 1)] for i in range(100)]
    direction_of_potential_history = [["none" for j in range(i + 1)] for i in range(100)]


    def get_bigger_potential_of_fathers(row, place):
        if row == 0:
            return 0
        if place == 0:
            direction_of_potential_history[row][place] = direction_of_potential_history[row - 1][place] + " left"
            return potential_of_100_triangle[row - 1][place]
        if place == row:
            direction_of_potential_history[row][place] = direction_of_potential_history[row - 1][place - 1] + " right"
            return potential_of_100_triangle[row - 1][place - 1]

        if potential_of_100_triangle[row - 1][place - 1] > potential_of_100_triangle[row - 1][place]:
            direction_of_potential_history[row][place] = direction_of_potential_history[row - 1][place - 1] + " right"
            return potential_of_100_triangle[row - 1][place - 1]
        else:
            direction_of_potential_history[row][place] = direction_of_potential_history[row - 1][place] + " left"
            return potential_of_100_triangle[row - 1][place]


    def get_potential_of_current(row, place):
        return get_bigger_potential_of_fathers(row, place) + triangle_of_100_levels[row][place]


    for i in range(100):
        for j in range(i + 1):
            potential_of_100_triangle[i][j] = get_potential_of_current(i, j)

    index_of_biggest_potential = potential_of_100_triangle[99].index(max(potential_of_100_triangle[99]))
    print(potential_of_100_triangle[99][index_of_biggest_potential])
    print(direction_of_potential_history[99][index_of_biggest_potential])