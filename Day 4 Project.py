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

#Write your code below this line 👇 

### Possible play scenarios
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock

### Choice clarification 
# Rock is choice 0
# Paper is choice 1
# Scissors is choice 2

you_win = False # initial set to run loop

while you_win == False: # Play until user wins
    ## Set random seed
    random.seed()

    ## Get computer choice
    computer_choice = random.randint(0, 2) 

    if computer_choice == 0:
        computer_choice = rock
    elif computer_choice == 1:
        computer_choice = paper
    elif computer_choice == 2:
        computer_choice = scissors
    else: #Error message
        print("Something went wrong!")

    ## Get user choice
    user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))

    if user_choice == 0:
        user_choice = rock
    elif user_choice == 1:
        user_choice = paper
    elif user_choice == 2:
        user_choice = scissors
    else: # Error message
        print("Something went wrong!")

    ## Compare choices (user to computer)
    # Reset you_win for comparison
    you_win = None
    you_tie = None

    # Cases where user loses or ties
    if user_choice == rock and computer_choice == paper: # rock lose
        you_win = False
    elif user_choice == scissors and computer_choice == rock: # scissors lose
        you_win = False
    elif user_choice == paper and computer_choice == scissors: # paper lose
        you_win = False
    elif user_choice == computer_choice: # tie
        you_win = False
        you_tie = True
    else: # All other scenarios are win scenarios
        you_win = True
        
    # Print results
    print(user_choice + '\n')
    print(f'Computer chose:\n{computer_choice}\n')
    
    if you_tie == True:
        print('You tie :|')
    elif you_win == False:
        print('You lose :(')
    elif you_win == True:
        print('You win!')
    
    
