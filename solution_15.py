# It's basically a Permutation of 40 spots: 20 right and 20 down
# You just need to decide where to place the 20 downs inside the 40 spots
# Therefore, 40!/[(40-20)! * 20!]


def fact(n):
    mult = 1
    for i in range(1, n+1):
        mult *= i
    return mult


if __name__ == '__main__':
    print(fact(40) / (fact(20) * fact(20)))
