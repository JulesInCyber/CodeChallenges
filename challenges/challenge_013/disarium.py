def disarium(number):
    # Starting Parameters
    i = 1
    sum = 0

    # Turn number into a list
    l = [int(d) for d in str(number)]
    for e in l:
        sum += e ** i
        i += 1
    
    if sum == number:
        return True
    else:
        return False

if __name__ == "__main__":
    print(disarium(135))