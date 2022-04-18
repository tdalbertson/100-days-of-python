import random
from hangman_art import logo, stages
from hangman_words import word_list

random.seed()
# Generate a random word
chosen_word = random.choice(word_list)
print(logo + "\nWelcome to Hangman!")

display = [] # For displaying the '_'
guessed_letters = [] # For keeping track of guessed letters
word_length = len(chosen_word)

for num in range(word_length):
    display += '_'

player_lives = 7
player_won = False

game_playing = True
while game_playing == True:
    print(f'Lives remaining: {player_lives} ')
    print(f"{' '.join(display)}")
    print(f"Letter bank: {' '.join(guessed_letters)}")
    guess = input('Please guess a letter: ').lower()

    for index in range(word_length):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = letter
            
    # Check if guess has already been guessed
    if guess in guessed_letters:
        print(f'\n\'{guess}\' was already tried.\n')
        guess = None
        continue
    else:
        guessed_letters.append(guess)
    
    if guess not in chosen_word:
        player_lives -= 1
        print(stages[player_lives])
        if player_lives == 0:
            print(f'You lost :(\nThe word was {chosen_word}.')
            break   
    
    if '_' not in display:
        player_won = True
        game_playing = False

if player_won:
    print(f'{display}\nYou won!')
