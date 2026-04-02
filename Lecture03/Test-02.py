#assignment 2

user_input = float(input("Enter inches to convert it into cms: "))

while user_input > 0:

    ans = user_input * 2.54
    print(ans)
    user_input = float(input("Enter inches to convert it into cms: "))
else:
    print("Your number is negative or 0 enter a valid number")