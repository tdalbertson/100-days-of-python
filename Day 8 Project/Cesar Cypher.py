import pyinputplus as pyip
from art import logo

# Function definitions
def encrypt_or_decrypt(choice, text, shift_num):
    new_text = ''
    
    for char in text:
        # For keeping characters not in the alphabet
        if char not in alphabet:
            new_text += char
            continue
        
        # Get index of char in alphabet
        position = alphabet.index(char)
        
        if choice == 'encode':
            # Create new position for each char in encrypted messaged
            new_position = position + shift_num
            
            # Checking if new position is out of range of alphabet
            if new_position > 25:
                new_position -= 26
                
        else: # To decode message
            # Create original position for each char to decrypt message
            new_position = position - shift_num
                
        new_text += alphabet[new_position]
            
    return new_text
        
    
# Main program flow
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

while(True):
    # Input checking
    direction = pyip.inputMenu(['encode', 'decode'], prompt="Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    # Gathering text to encode/decode and shift number
    text = input("Type your message:\n").lower()
    
    # For preventing shifts outside of range
    shift = pyip.inputNum(prompt="Type the shift number:\n", max=26)
    # For allowing shifts over 26 use shift = shift % 26
        
    message = encrypt_or_decrypt(direction, text, shift)

    print(f'The message is "{message}".')
    
    go_again = pyip.inputYesNo(prompt="Type 'yes' if you want to go. Otherwise type 'no'.\n")
    
    if go_again == 'no':
        print('Goodbye 👋')
        break
