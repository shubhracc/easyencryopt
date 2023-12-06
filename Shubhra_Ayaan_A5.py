"""This encryption program gives the user four options.

Option 1 is for encryption using a plain text and a key.
Option 2 is for decyption using a cipher text and a key.
Option 3 is for generating a key with a specified length.
Option 4 is for quitting the program.
"""

__author__ = "Shubhra Chowdhury, Ayaan Adrito"

import random

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def print_menu():
    """Prints the program's menu with options ranging from 1-4."""
    print("""Please choose from one of the following menu options:
1. Encrypt plaintext.
2. Decrypt ciphertext.
3. Generate key.
4. Exit.""")

def validate_input(num_one: int, num_two: int, err_msg_one: str, err_msg_two: str) -> int:
    """Validate input and return an integer between num_one and num_two.
    Print err_msg_one if input is not and int.Print err_msg_two if int is out of range."""

    print_menu()

    while True:
        while True:    
            try:
                primary_input = int(input(">"))
                break
            except ValueError:
                print(err_msg_one)
        if 1 <= primary_input <= 4:
            return primary_input
        else:
            print(err_msg_two)    

def auto_corrector(text:str) -> str:
    """Go through all of text and check every single character to see if it's a letter.  
    If it is not a letter get rid of it.
    
    >>> auto_corrector("ABCJSHD@#(I#2$SDA)")
    ABCJSHDSDA
    """

    text = text.upper()
    new_text = ""

    for i in range(len(text)):
        if 65 <= ord(text[i]) <= 90:
            new_text += text[i]
        else:
            pass

    return(new_text)


def add_spaces(text:str, spacer:int) -> str:
    """add a space every 5th character
    
    >>> add_spaces("ABCDEFGHIJKLM", 5)
    ABCDE FGHIJ KLM
    """

    spaced_text = ''
    for i in range(0, len(text), spacer):
        spaced_text += text[i:i+spacer] + ' '
    return spaced_text




def plain_text_encryptor(spacer, ALPHABET, final_message) -> str:
    """"""
    
    plain_text = input("Please enter text to encrypt: ")
    new_text = auto_corrector(plain_text)
    print_text = add_spaces(new_text, spacer)
    print("This is the plaintext: {}".format(print_text))

    key = input("A key is any string of letters (1-500 chars): ")
    new_key = auto_corrector(key)
    print("Using encryption key: {}".format(new_key))

    for char_1 in new_text:
        for char in new_key:
            shift = (ALPHABET.index(char) + 1)
            new_text_letter = ALPHABET.index(char_1)
            new_char = shift + new_text_letter
            if new_char > 26:
                new_char -= 26
            else:
                pass
            final_message += ALPHABET[new_char]

    if (len(final_message)) % 5 != 0:
        num_filler_num = (len(final_message)) % 5
        for i in range(num_filler_num):
            filler_num = random.randint(0, 26)
            final_message += ALPHABET[filler_num]

    print(add_spaces(final_message, 5))

def main():


    SPACER = 5

    playing = True

    while playing == True:
        final_message = ""
        print("""----------------------------------
EasyCrypt Text Encryptor/Decryptor
----------------------------------""")
        primary_input = validate_input(1, 4, "invalid input", "Invalid choice. Try again.")
        if primary_input == 1:
            plain_text_encryptor(SPACER, ALPHABET, final_message)
        #if primary_input == 2:
        
        #if primary_input == 3:
        
        #if primary_input == 4:
            playing = False
            break


if __name__ == "__main__":
    main()