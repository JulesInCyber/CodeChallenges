def tribonacci(pos):

    # Special Cases
    if pos == 0:
        return 0
    elif pos == 1 or pos == 2:
        return 1
    
    # Initializing the first three numbers
    t0 = 0
    t1 = 1
    t2 = 1

    for i in range(3, pos+1):
        t_pos = t0 + t1 + t2
        t0 = t1
        t1 = t2
        t2 = t_pos
    return t_pos

if __name__ == "__main__":
    tx = input("Enter the position of the Tribonacci Number: ")
    result = tribonacci(int(tx))
    print(result)