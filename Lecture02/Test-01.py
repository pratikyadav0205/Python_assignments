#Assignment 1

length = float(input("Enter the length of the zander in centimeters: "))

limit = 42

if length < limit:
    short = limit - length
    print("The zander is too small.")
    print(f"Release the fish back into the lake. It is {short:.1f} cm short than the limit.")
else:
    print("The zander meets the limit size. You can keep it.")