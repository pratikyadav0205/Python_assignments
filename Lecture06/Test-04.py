def remove_odds(numbers):
    return [num for num in numbers if num % 2 == 0]


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    new_list = remove_odds(numbers)

    print("Original list:", numbers)
    print("Even numbers only:", new_list)


main()
