#Assignment 2

user_class = input("Enter cabin class (LUX, A, B, C): ").upper()

if user_class == "LUX":
    print("Upper-deck cabin with a balcony.")
elif user_class == "A":
    print("Cabin above the car deck with a window.")
elif user_class == "B":
    print("Windowless cabin above the car deck.")
elif user_class == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class")
