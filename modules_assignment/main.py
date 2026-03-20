import math_utlis
from math_utlis import square

print("add (10 & 5):", math_utlis.add(10, 5))
print("subtract(10, 5):", math_utlis.subtract(10, 5))
print("square(4):", square(4))


import string_utils

text = input("Write anything: ")
print("original:", text)
print("capitalized:", string_utils.capitalize_words(text))
print("reversed:", string_utils.reverse_string(text))
print("word count:", string_utils.word_count(text))

import shop_package

items = [100, 200, 300, 400]
total = shop_package.calculate_total(items)
print("Total before tax/discount:", total)

# Apply 10% discount
discounted = shop_package.apply_discount(total, 10)
print("Total after 10% discount:", discounted)

# Apply 5% tax
final_bill = shop_package.apply_tax(discounted)
print("Final Bill (with tax):", final_bill)

import shop_package.discount as disc
from shop_package.billling  import calculate_total, apply_tax

print("Discount (10% of 1000):", disc.apply_discount(1000, 10))
print("Flat Discount (500 - 50):", disc.flat_discount(500))

prices = [100, 200, 300]
total = calculate_total(prices)
print("Calculate Total:", total)
print("Apply Tax (5%):", apply_tax(total))
