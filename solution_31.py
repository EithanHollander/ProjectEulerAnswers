if __name__ == '__main__':

    def find_all_dividing_options_1(x):
        sum = 0
        for a1 in range(0, x+1):
            for b2 in range(0, int(x/2) + 1):
                if 1*a1 + 2*b2 > x:
                    break
                for c5 in range(0, int(x/5) + 1):
                    if 1*a1 + 2*b2 + 5*c5 > x:
                        break
                    for d10 in range(0, int(x/10) + 1):
                        if 1*a1 + 2*b2 + 5*c5 + 10*d10 > x:
                            break
                        for e20 in range(0, int(x/20) + 1):
                            if 1*a1 + 2*b2 + 5*c5 + 10*d10 + 20*e20 > x:
                                break
                            for f50 in range(0, int(x/50) + 1):
                                if 1*a1 + 2*b2 + 5*c5 + 10*d10 + 20*e20 + 50*f50 > x:
                                    break
                                for g100 in range(0, int(x/100) + 1):
                                    if 1*a1 + 2*b2 + 5*c5 + 10*d10 + 20*e20 + 50*f50 + 100*g100 > x:
                                        break
                                    for h200 in range(0, int(x/200) + 1):
                                        y = 1*a1 + 2*b2 + 5*c5 + 10*d10 + 20*e20 + 50*f50 + 100*g100 + 200*h200
                                        if y > x:
                                            break
                                        elif y == x:
                                            sum += 1
                                            print(a1,b2,c5,d10,e20,f50,g100,h200)
        return sum



    # Other Algorithms I found online and really liked: (I think those are better than mine)
    # But at least mine actually shows all the options of how many to take from each coin :P
    # Fast!
    def find_all_dividing_options_2(x):
        sum = 0
        for a in range(x, -1, -200):
            for b in range(a, -1, -100):
                for c in range(b, -1, -50):
                    for d in range(c, -1, -20):
                        for e in range(d, -1, -10):
                            for g in range(e, -1, -5):
                                for h in range(g, -1, -2):
                                    sum += 1
        return sum

    # Generic!
    def find_all_dividing_options_3(x, coins):
        if not coins: return 0
        c, coins = coins[0], coins[1:]
        count = 0
        if x % c == 0:
            count += 1
        for amount in range(0, x, c):
            count += find_all_dividing_options_3(x - amount, coins)
        return count

    print(find_all_dividing_options_1(200))
    # print(find_all_dividing_options_2(200))
    # print(find_all_dividing_options_3( 200, (1,2,5,10,20,50,100,200)))
