#assignment 3

num = input("Enter a number (press Enter to stop): ")

if num != "":
    smallest = int(num)
    largest = int(num)

    while True:
        num = input("Enter a number (press Enter to stop): ")

        if num == "":
            break
        num = int(num)
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    print("Smallest number:", smallest)
    print("Largest number:", largest)

else:
    print("No numbers were entered.")


