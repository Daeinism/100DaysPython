bill = 0
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
photos = input("Do you want photos? Y or N ")

if height > 120:
    if age < 12:
        bill += 5
    elif age < 18:
        bill += 7
    elif age >= 45 and age <= 55:
        bill += 0
    else:
        bill += 12
    if photos == "Y":
        bill += 3
    print(f"Your total bill is ${bill}")
else:
    print("You can't ride")
