"""This encryption program gives the user four options.

Option 1 encypts plain text using a key.
Option 2 is for decrypting a cipher text using a key.
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

def validate_input(num1: int, num2: int, msg1: str, msg2: str) -> int:
    """Validate input and return an integer between num1 and num2.
    Print erorr message 1: msg1 if input is not and int.
    Print erorr message 2: msg2 if int is out of range."""

    valid = False

    print_menu()

    while valid == False:
        while True:    
            try:
                primary_input = int(input("> "))
                break
            except ValueError:
                print(msg1)
        if num1 <= primary_input <= num2:
            valid = True
        else:
            print(msg2)
            valid = False
    return(primary_input) 

def clean_text(text: str) -> str:
    """Return text with letters only and uppercased.
    
    >>> clean_text('ABCJSHD@#(I#2$SDA)')
    ABCJSHDSDA

    >>> clean_text('cH1+ick#en')
    CHICKEN
    """

    text = text.upper()
    new_text = ""

    for char in text:
        if 65 <= ord(char) <= 90:
            new_text += char
        else:
            pass

    return(new_text)


def add_spaces(text: str, spacer: int) -> str:
    """Add a space to text every spacer characters.
    
    >>> add_spaces('ABCDEFGHIJKLM', 5)
    'ABCDE FGHIJ KLM'

    >>> add_spaces('HELLOFRIEND', 3)
    'HEL LOF RIE ND'
    """

    spaced_text = ''
    for i in range(0, len(text), spacer):
        spaced_text += text[i:i+spacer] + ' '
    return spaced_text

def encrypt_text(plain_text: str, key: str) -> str:
    """Encrypt message plain_text using encoder key.
    
    >>> encrypt('HELLO', 'NZXTN')
    'VEJFC'

    >>> encrypt('DRAGON BALL', 'DBZ')
    'HTAKQ NFCLP'
    """

    result = ""
    key_counter = 0

    for i in range(len(plain_text)):
        if key_counter <= len(key):
            key_counter = 0

        shift = ALPHABET.index(key[key_counter]) + 1
        new_char = (ALPHABET.index(plain_text[i]) + shift) % 25
        result += ALPHABET[new_char]

        key_counter += 1

    return result

def decrypt_text(cipher_text: str, key: str) -> str:
    """Decrypt_text message cipher_text using decoder key.
    
    >>> encrypt('VEJFC', 'NZXTN')
    'HELLO'

    >>> encrypt('HTAKQ NFCLP', 'DBZ')
    'DRAGON BALL'
    """

    result = ""
    key_counter = 0

    for i in range(len(cipher_text)):
        if key_counter <= len(key):
            key_counter = 0

        shift = ALPHABET.index(key[key_counter]) + 1
        new_char = (ALPHABET.index(cipher_text[i]) - shift)

        if new_char < 0:
            new_char += 25

        result += ALPHABET[new_char]

        key_counter += 1

    return result

def main():
    SPACER = 5
    running = True

    while running == True:
        final_message = ""
        print("""----------------------------------
EasyCrypt Text Encryptor/Decryptor
----------------------------------""")
        primary_input = validate_input(1, 4, "invalid input", "Invalid choice. Try again.")
        if primary_input == 1:

            plain_text = input("Please enter text to encrypt: ")
            plain_text = clean_text(plain_text)

            print_text = add_spaces(plain_text, SPACER)
            print("This is the plaintext: {}".format(print_text))

            while True:
                key = input("A key is any string of letters (1-500 chars): ")
                key = clean_text(key)

                if 1 <= len(key) <= 500:
                    break
                else:
                    print("invalid length")
            print("Using encryption key: {}".format(key))

            final_message = encrypt_text(plain_text, key)
            print(final_message)
        if primary_input == 2:
            cipher_text = input("Please enter text to decrypt: ")
            cipher_text = clean_text(plain_text)

            cipher_text = add_spaces(plain_text, SPACER)
            print("This is the plaintext: {}".format(print_text))

            while True:
                key = input("A key is any string of letters (1-500 chars): ")
                key = clean_text(key)

                if 1 <= len(key) <= 500:
                    break
                else:
                    print("invalid length")
            print("Using encryption key: {}".format(key))

            final_message = decrypt_text(cipher_text, key)
            print(final_message)
        if primary_input == 3:
            print("Generate key")
        if primary_input == 4:
            running = False
            break


if __name__ == "__main__":
    main()