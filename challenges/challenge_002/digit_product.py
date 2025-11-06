import sys
from termcolor import colored

# Function
def multiply_digits(n):
    l = list(n)
    product = 1
    for i in l:
        try:
            int_num = int(i)
            product = product * int_num
        except:
            raise TypeError(colored(
                "[!] ~ Only Integers are allowed!",
                "red", 
                attrs=["bold"]))
    print(product)


if __name__ == '__main__':
    # Get Command line Argument
    number = sys.argv[1]

    # Apply function
    multiply_digits(number)


# Comment
# Comment 2