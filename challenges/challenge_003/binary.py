import sys

operation = sys.argv[1]
number = sys.argv[2]

def encode(decimal_string):
    integer = int(number)
    remainder = []

    while integer != 0:
        remainder.append(str(integer % 2))
        integer = integer // 2

    binary = "".join(reversed(remainder))
    return binary

def decode(binary_string):
    decimal = 0
    length = len(binary_string)
    
    for i in range(length):
        power = length - 1 - i
        decimal += int(binary_string[i]) * (2 ** power)
    return decimal

if __name__ == "__main__":
    if operation == "encode":
        result = encode(number)
    elif operation == "decode":
        result = decode(number)

print(result)