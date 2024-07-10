#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
numLetters= int(input("How many letters would you like in your password?\n")) 
numSymbols = int(input(f"How many symbols would you like?\n"))
numNumbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []

for num in range (0,numLetters):
  ranNum = random.randint(0,len(letters)-1)
  password += letters[ranNum]

for num in range (0,numSymbols):
  ranNum = random.randint(0,len(symbols)-1)
  password += symbols[ranNum]

for num in range (0,numNumbers):
  ranNum = random.randint(0,len(numbers)-1)
  password += numbers[ranNum]

random.shuffle(password)

output = ""
for num in range (0,len(password)):
  output += str(password[num])
print(f"Your password is {output}")

output2 = ""
for char in password:
  output2 += char
print(f"Your password is {output2}")