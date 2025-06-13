while True:
    num = int(input("Enter a number: "))
    if num > 21:
        print("This number is invalid")
    else:
        print(f"{num}")
        for i in range(1,11):
            print(f"{num} x {i} = {num * i}")
