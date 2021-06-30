if __name__ == '__main__':
    numbers_to_words = {
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand"
    }

    def build_word_of_number(num):
        if num <= 20:
            return numbers_to_words[num]
        if num <= 99:
            if num % 10 == 0:
                return numbers_to_words[num]
            return numbers_to_words[int(num / 10) * 10] + '-' + numbers_to_words[num % 10]
        if num <= 999:
            if num % 100 == 0:
                return numbers_to_words[int(num / 100)] + ' ' + numbers_to_words[100]
            return numbers_to_words[int(num / 100)] + ' ' + numbers_to_words[100] + ' and ' + build_word_of_number(num % 100)
        if num == 1000:
            return 'one ' + numbers_to_words[1000]

    all_words_of_nums_until_1000 = []
    for i in range(1, 1001):
        all_words_of_nums_until_1000.append(build_word_of_number(i))

    all_words_of_nums_until_1000_replaced = []
    for word in all_words_of_nums_until_1000:
        all_words_of_nums_until_1000_replaced.append(word.replace(' ', '').replace('-', ''))

    print(sum(len(x) for x in all_words_of_nums_until_1000_replaced))
