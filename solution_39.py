import math


if __name__ == '__main__':

    def find_amount_of_triangle_solutions(p):
        sum = 0
        for a in range(1, int(p/2)):
            for b in range(a, int(p/2)):
                c = math.sqrt(a*a + b*b)
                if a + b + c > p:
                    break
                if a + b + c == p:
                    sum += 1
        return sum


    def find_perimeter_with_max_amount_of_triangles(max_p):
        max_amount = 0
        max_ip = 0
        for ip in range(1, max_p+1):
            print(ip)
            current_amount = find_amount_of_triangle_solutions(ip)
            if current_amount > max_amount:
                max_amount = current_amount
                max_ip = ip

        return max_ip


    print(find_perimeter_with_max_amount_of_triangles(1000))
