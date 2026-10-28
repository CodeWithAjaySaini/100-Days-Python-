import random
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
random_computer_number = random.randint(0, 2)
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_input == 0:
    print(f'\n{rock}')
    if random_computer_number == 0:
        print("Computer chose:")
        print(f'\n{rock}')
        print("Computer chose Same")
    elif random_computer_number == 1:
        print("Computer chose:")
        print(f'\n{paper}')
        print("You Lose")

    elif random_computer_number == 2:
        print("Computer chose:")
        print(f'\n{scissors}')
        print("You Won")

    else:
        print("Invalid choice")

if user_input == 1:
    print(f'\n{paper}')
    if random_computer_number == 0:
        print("Computer chose:")
        print(f'\n{rock}')
        print("You Won")
    elif random_computer_number == 1:
        print("Computer chose:")
        print(f'\n{paper}')
        print("Same choice")

    elif random_computer_number == 2:
        print("Computer chose:")
        print(f'\n{scissors}')
        print("You Lose")

    else:
        print("Invalid choice")

if user_input == 2:
    print(f'\n{scissors}')
    if random_computer_number == 0:
        print("Computer chose:")
        print(f'\n{rock}')
        print("You Lose")
    elif random_computer_number == 1:
        print("Computer chose:")
        print(f'\n{paper}')
        print("you Won")

    elif random_computer_number == 2:
        print("Computer chose:")
        print(f'\n{scissors}')
        print("Same choose")

    else:
        print("Invalid choice")
