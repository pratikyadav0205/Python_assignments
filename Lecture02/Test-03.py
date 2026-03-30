#Assignment 3

gender = input("Enter your biological gender (male/female): ").lower()

hb = float(input("Enter your hemoglobin level (g/L): "))

if gender == "female":
    if hb < 117:
        print("Hemoglobin level is low.")
    elif 117 <= hb <= 155:
        print("Hemoglobin level is normal.")
    else:
        print("Hemoglobin level is high.")

elif gender == "male":
    if hb < 134:
        print("Hemoglobin level is low.")
    elif 134 <= hb <= 167:
        print("Hemoglobin level is normal.")
    else:
        print("Hemoglobin level is high.")

else:
    print("Invalid gender input.")