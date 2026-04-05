num = int(input("Enter an integer: "))

if num < 2:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")