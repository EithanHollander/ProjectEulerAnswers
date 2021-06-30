from solution_15 import fact

fact_of_digit = [fact(x) for x in range(10)]

def find_sum_of_digits_facts(x):
    sum = 0
    for c in str(x):
        #  I used a pre-defined array to save computing time
        sum += fact_of_digit[int(c)]
    return sum


if __name__ == '__main__':
    #  Same as solution_30, 9! = 362880, so for x-digit number the max of facts-sum is x*9!
    #  the max facts-sum for a 7-digit number is facts_sum(9_999_999) which is 7*9!=2_540_160, much smaller than 9_999_999
    #  therefore no need to look further than that number
    #  A real and way faster upper bound would be 50,000, but you would only know that after you have seen the solution and that's not fun :)
    i = 3
    sum = 0
    while i < 9_999_999:
        if i == find_sum_of_digits_facts(i):
            sum += i
        i += 1

    print(sum)
