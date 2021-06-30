if __name__ == '__main__':
    all_cubes_sorted = {}
    optional_minimal_cubes = []
    i = 1
    max_len = 0
    while True:
        cube = i * i * i
        cube_str = ''.join(sorted(str(cube)))
        if max_len and len(cube_str) > max_len:
            break
        all_cubes_sorted.setdefault(cube_str, [0, []])
        all_cubes_sorted[cube_str][0] += 1
        all_cubes_sorted[cube_str][1].append(cube)
        if all_cubes_sorted[cube_str][0] == 5:
            if not max_len:
                max_len = len(cube_str)
            optional_minimal_cubes.append(all_cubes_sorted[cube_str][1][0])
            # print(cube_str, len(cube_str))
            # print(all_cubes_sorted[cube_str])
            # print("--------------------------------")
        i += 1

    print(min(optional_minimal_cubes))