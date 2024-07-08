rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

gameImage = [rock, paper, scissors]

userAction = int(input(
    "What do you choose?\nType 0 - Rock\nType 1 - Paper\nType 2 - Scissors\n"))
if userAction >= 0 and userAction <= 2:

    ranNum = random.randint(0, 2)
    print(gameImage[userAction])
    print("Computer Chose:\n")
    print(gameImage[ranNum])

    if userAction == 0:
        if ranNum == 0:
            print("It's a draw")
        elif ranNum == 1:
            print("You Lose")
        elif ranNum == 2:
            print("You Win")
    elif userAction == 1:
        if ranNum == 0:
            print("You Win")
        elif ranNum == 1:
            print("It's a draw")
        elif ranNum == 2:
            print("You Lose")
    elif userAction == 2:
        if ranNum == 0:
            print("You Lose")
        elif ranNum == 1:
            print("You Win")
        elif ranNum == 2:
            print("It's a draw")
else:
    print("You typed an invalid number, you lose!")