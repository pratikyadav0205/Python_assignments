talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

# converting into lots first
total_lots = (talents * 20 * 32) + (pounds * 32) + lots

# lots to grams
total_grams = total_lots * 13.3


kg = int(total_grams // 1000)
g = total_grams % 1000

print("\nThe weight in modern units:")
print(kg, "kilograms and", round(g, 2), "grams.")
