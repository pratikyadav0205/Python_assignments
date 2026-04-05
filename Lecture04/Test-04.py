cities = []

for i in range(5):
    user_input = input("Enter the name of city:")
    cities.append(user_input)

print("Here are the cities entered by the user...")
for city in cities:
    print(city)