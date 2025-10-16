"""
Write a function that takes accepts one parameter.
The given Parameter will be a string of a multi-digit number.
The function should return the product of all digits.

1234 -> 24
1111 -> 1
"""
import sys

# Function
def multiply_digits(n):
    l = list(n)
    product = 1
    for i in l:
        try:
            int_num = int(i)
            product = product * int_num
        except:
            raise TypeError("Only Integers are allowed!")
    print(product)


if __name__ == '__main__':
    # Get Command line Argument
    number = sys.argv[1]

    # Apply function
    multiply_digits(number)
