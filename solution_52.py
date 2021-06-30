if __name__ == '__main__':
    found_the_chosen_number = False
    x = 1
    while not found_the_chosen_number:
        if (''.join(sorted(str(x))) ==
            ''.join(sorted(str(2*x))) ==
            ''.join(sorted(str(3*x))) ==
            ''.join(sorted(str(4*x))) ==
            ''.join(sorted(str(5*x))) ==
            ''.join(sorted(str(6*x)))):
            found_the_chosen_number = True
            print(x)
        x += 1