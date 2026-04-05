import random

num_of_dice = int(input("Enter the number of dice you want to roll: "))

total = 0

for i in range(num_of_dice):
    roll = random.randint(1,6)
    print(roll)
    total = roll + total

print("Sum of the dice:", total)

