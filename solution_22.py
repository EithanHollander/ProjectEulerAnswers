def get_alphabetical_position(letter):
    return ord(letter) - ord('A') + 1


def sum_of_alphabetical_positions(word):
    return sum([get_alphabetical_position(l) for l in word])


if __name__ == '__main__':

    with open("problem_22_names.txt") as names:
        all_names_raw = []
        for line in names.readlines():
            all_names_raw.extend(line.split(","))
        all_names_netto = []
        for name in all_names_raw:
            all_names_netto.append(name.replace("\"", ""))
        all_names_netto.sort()
        print(sum((all_names_netto.index(x)+1) * sum_of_alphabetical_positions(x) for x in all_names_netto))
