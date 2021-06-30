import math
from solution_22 import sum_of_alphabetical_positions


def is_triangle_number(number):
    return math.sqrt(8*number + 1) % 2 == 1


if __name__ == '__main__':
    with open("problem_42_words.txt") as names:
        all_words_raw = []
        for line in names.readlines():
            all_words_raw.extend(line.split(","))
        all_words_netto = []
        for name in all_words_raw:
            all_words_netto.append(name.replace("\"", ""))
        print(sum([is_triangle_number(sum_of_alphabetical_positions(word)) for word in all_words_netto]))
