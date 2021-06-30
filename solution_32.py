from solution_15 import fact
from solution_24 import get_the_permutation_in_place_of

def find_all_multiplicand_multiplier_product(str_of_number):
    second_half = len(str_of_number) - len(str_of_number) // 2
    return [(str_of_number[:i], str_of_number[i: second_half], str_of_number[second_half:]) for i in range(1, second_half)]

def find_product_of_pandigital_number(pandigital_number):
    for multiplicand, multiplier, product in find_all_multiplicand_multiplier_product(str(pandigital_number)):
        if int(multiplicand) * int(multiplier) == int(product):
            return product
    return None

def sum_of_all_prodcuts(all_digits):
    all_products = set()
    for num in range(0, fact(len(all_digits))):
        product = find_product_of_pandigital_number(get_the_permutation_in_place_of(num, all_digits))
        if product:
            all_products.add(int(product))
    return sum(all_products)

print(sum_of_all_prodcuts(["1", "2", "3", "4", "5", "6", "7", "8", "9"]))