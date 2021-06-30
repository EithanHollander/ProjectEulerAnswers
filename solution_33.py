from fractions import Fraction

if __name__ == '__main__':
    product_of_all_curious_fractions = 1

    for digit_to_be_cancelled in range(1, 10):
        for top_digit in range(1, digit_to_be_cancelled):
            for bottom_digit in range(1, 10):
                # print(str(top_digit) + str(digit_to_be_cancelled), str(digit_to_be_cancelled) + str(bottom_digit))
                if bottom_digit * (10 * top_digit + digit_to_be_cancelled) == top_digit * (10 * digit_to_be_cancelled + bottom_digit):
                    product_of_all_curious_fractions *= top_digit / bottom_digit
        #  We don't need to check cases as xx/xy when y>x
        #  Because xx/xy will always be bigger than 9/10 (since xy-xx < 10 and xy > 10)
        #  And x/y - as x,y are just two normal digits - couldn't be bigger than 9/10

    print(Fraction(product_of_all_curious_fractions).limit_denominator().denominator)