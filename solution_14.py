if __name__ == '__main__':

    def next_step(n):
        if n % 2 == 0:
            return n/2
        else:
            return 3*n + 1

    def make_sequence_and_return_length(start):
        length_of_seq = 1
        while True:
            if start == 1:
                break
            start = next_step(start)
            length_of_seq += 1
        return length_of_seq


    max_len_of_seq = 0
    start_num_with_biggest_len_of_seq = 0
    for i in range(1, 1_000_000):
        temp_len = make_sequence_and_return_length(i)
        if temp_len > max_len_of_seq:
            max_len_of_seq = temp_len
            start_num_with_biggest_len_of_seq = i

    print(start_num_with_biggest_len_of_seq)
