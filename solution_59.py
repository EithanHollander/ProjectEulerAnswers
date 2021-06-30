from operator import xor

if __name__ == '__main__':

    def encrypt(message, key):
        # takes message and key, both with numbers inside
        encrypted = []
        for i in range(0, len(message)):
            encrypted.append(xor(message[i], key[i % len(key)]))
        return encrypted

    def check_english(number):
        return (32 <= number <= 90) or (97 <= number <= 122)

    with open("problem_59_encrypted.txt") as to_encrypt:
        all_chars_raw = to_encrypt.read().strip().split(",")
        # making the chars into numbers
        all_chars_raw = [int(x) for x in all_chars_raw]

        # NOTE: All 'letters' are represented by their ascii values
        english_letters = range(ord('a'), ord('z') + 1)

        first_letter_of_key = set([])
        for letter in english_letters:
            # Trying all possible letter for the first letter in the key
            for place_in_file in range(0, len(all_chars_raw), 3):
                first_letter_of_key.add(letter)
                # Even if one letter was not encrypted to english in this whole session
                # it means that the current letter shall not be the first letter of the key
                if not check_english(xor(all_chars_raw[place_in_file], letter)):
                    first_letter_of_key.remove(letter)
                    break

        second_letter_of_key = set([])
        for letter in english_letters:
            # Trying all possible letter for the second letter in the key
            for place_in_file in range(1, len(all_chars_raw), 3):
                second_letter_of_key.add(letter)
                # Even if one letter was not encrypted to english in this whole session
                # it means that the current letter shall not be the second letter of the key
                if not check_english(xor(all_chars_raw[place_in_file], letter)):
                    second_letter_of_key.remove(letter)
                    break

        third_letter_of_key = set([])
        for letter in english_letters:
            # Trying all possible letter for the third letter in the key
            for place_in_file in range(2, len(all_chars_raw), 3):
                third_letter_of_key.add(letter)
                # Even if one letter was not encrypted to english in this whole session
                # it means that the current letter shall not be the third letter of the key
                if not check_english(xor(all_chars_raw[place_in_file], letter)):
                    third_letter_of_key.remove(letter)
                    break

        final_key = list()
        final_key.append(list(first_letter_of_key)[0])
        final_key.append(list(second_letter_of_key)[0])
        final_key.append(list(third_letter_of_key)[0])

        encrypted_text = encrypt(all_chars_raw, final_key)
        print(sum(encrypted_text))