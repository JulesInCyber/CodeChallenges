import sys

operation = sys.argv[1]
number = sys.argv[2]

def encode(number):
    integer = int(number)
    remainder = []

    while integer != 0:
        remainder.append(str(integer % 2))
        integer = integer // 2

    binary = "".join(reversed(remainder))
    return binary

def decode(number):
    pass

if __name__ == "__main__":
    if operation == "encode":
        result = encode(number)

print(result)