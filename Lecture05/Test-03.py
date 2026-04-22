airports = {}

while True:
    print("\n1. Add airport")
    print("2. Fetch airport")
    print("3. Quit")

    choice = input("Choose option: ")

    if choice == "1":
        icao = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[icao] = name
        print("Airport saved!")

    elif choice == "2":
        icao = input("Enter ICAO code: ")
        if icao in airports:
            print(airports[icao])
        else:
            print("Airport not found")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option")