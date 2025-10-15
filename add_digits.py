"""
Write a function that takes accepts one parameter.
The given Parameter will be a string of a multi-digit number.
The function should return the product of all digits.

1234 -> 24
1111 -> 1
"""
import sys

number = sys.argv[1]
number_list = list(number)

prod = 1
for i in number_list:
    prod = int(i) * prod

print(prod) 
