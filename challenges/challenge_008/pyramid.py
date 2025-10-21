def pyramid(n):
    for i in range(n+1):
        print(i*f"{n}")

if __name__ == "__main__":
    height = input("Enter height of pyramid: ")
    pyramid(int(height))