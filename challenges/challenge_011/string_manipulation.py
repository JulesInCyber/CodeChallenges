input_string = "IN/25/MAR/10/ZZ/DE"

split = input_string.split("/")
split = split[:4]

returned = " ".join(split)

print(returned)
