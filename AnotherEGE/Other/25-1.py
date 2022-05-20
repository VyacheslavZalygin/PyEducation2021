for m in range(1, 28+1, 2):
    for n in range(0, 18+1, 2):
        number = 2**m * 3**n
        if 150000000 <= number <= 300000000:
            print(number)