if __name__ == '__main__':
    print(6531031914842725)
    # I solved it WITHOUT CODING!!!
    # I knew all the bigger numbers should be on the outside in order to get the maximal string, and also 10 must be on the outside - size of final answer should be 16 chars long
    # Which means the insides are 1,2,3,4,5 - total of 15, the rest are total of 40
    # Therefore, the sum we need is (15*2 + 40)/5 = 70/5 = 14 [inside counted twice, then we have to dividfe it to 5 equal trios)
    # we know 5 and 4 can't be next to each other because the sum needs to be 14 and we don't have two 5's
    # we also know 1 and 2 can't be next to each other because we need 14 and we don't have an 11
    # therefore the order of the centers must around the 3 - either 1,5 are to its left,right and then the 2,4 are on the opposite sides
    # or the 1,5 are to its right,left and the 2,4 are on the opposite sides.
    # => 3,5,2,4,1 or 3,1,4,2,5 (circled)
    # then, you just complete the numbers to 14 and you get two options, starting from 6, the smallest number of the bigger numbers:
    # 653|1031|914|842|725 or 635|752|824|941|1013 => first option is bigger so it's taken. That's it!
