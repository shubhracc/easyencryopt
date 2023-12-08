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

def validate_input(num1: int, num2: int, msg: str, err_msg1: str, err_msg2: str) -> int:
    """Validate input and return an integer between num1 and num2.
    Print erorr message 1: err_msg1 if input is not and int.
    Print erorr message 2: err_msg2 if int is out of range."""

    valid = False

    while valid == False:
        while True:    
            try:
                primary_input = int(input(msg))
                break
            except ValueError:
                print(err_msg1)
        if num1 <= primary_input <= num2:
            valid = True
        else:
            print(err_msg2)
            valid = False
    return(primary_input) 

def clean_text(text: str) -> str:
    """Return text with letters only and uppercased.
    
    >>> clean_text('ABCJSHD@#(I#2$SDA)')
    'ABCJSHDSDA'

    >>> clean_text('cH1+ick#en')
    'CHICKEN'
    """

    text = text.upper()
    new_text = ""

    for char in text:
        # 65 and 90 are the ascii values for between A and Z
        if 65 <= ord(char) <= 90:
            new_text += char
        else:
            pass

    return(new_text)

def random_char(num1: int, num2: int) -> str:
    """Generate a random character betweet ASCII values num1 and num2
    and return it."""

    return chr(random.randint(num1, num2))

def add_filler(text: str, num: int) -> str:
    """Add random letters to text until its length
    is divisible by num.

    >>> filler_text('HELL', 5)
    'HELLT'
    >>> filler_text('RECTANGLE', 4)
    'RECTANGLEQSF'
    """

    result = text
    while len(result) % num != 0:
        result += random_char(65, 90)

    return result

def generate_key(num: int) -> str:
    """Generate and return a key with a length of num"""

    result = ""
    while len(result) <= num:
        result += random_char(65, 90)

    return result

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
        if key_counter >= len(key):
            key_counter = 0

        # Calculate how many spaces to shift by
        shift = ALPHABET.index(key[key_counter]) + 1
        # Shift the current character to make the encrypted charcter
        new_char = (ALPHABET.index(plain_text[i]) + shift) % 26
        result += ALPHABET[new_char]

        key_counter += 1

    # Add filler text to result before returning it spaced out
    return add_spaces(add_filler(result, 5), 5)

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
        if key_counter >= len(key):
            key_counter = 0

        # Calculate how many spaces to shift by
        shift = ALPHABET.index(key[key_counter]) + 1
        # Shift the current character to make the decrypted charcter
        new_char = (ALPHABET.index(cipher_text[i]) - shift)

        # Shift character sharting from Z if less than A
        if new_char < 0:
            new_char += 26

        result += ALPHABET[new_char]

        key_counter += 1

    # Add spaces every 5 characters before returning
    return add_spaces(result, 5)

def main():
    SPACER = 5
    running = True

    print("""----------------------------------
EasyCrypt Text Encryptor/Decryptor
----------------------------------""")

    while running == True:

        final_message = ""
        print_menu()
        primary_input = validate_input(1, 4, "> ", "invalid input", "Invalid choice. Try again.")

        if primary_input == 1:
            plain_text = input("\nPlease enter text to encrypt: ")
            plain_text = clean_text(plain_text)

            print_text = add_spaces(plain_text, SPACER)
            print(f"This is the plaintext: {print_text}\n")

            while True:
                key = input("A key is any string of letters (1-500 chars): ")
                key = clean_text(key)

                if 1 <= len(key) <= 500:
                    break
                else:
                    print("invalid length")
            print(f"Using encryption key: {key}\n")

            final_message = encrypt_text(plain_text, key)
            print(f"Your message has been encrypted:\n{final_message}\n")
        if primary_input == 2:
            cipher_text = input("\nPlease enter text to decrypt: ")
            cipher_text = clean_text(cipher_text)

            print_text = add_spaces(cipher_text, SPACER)
            print(f"This is the plaintext: {print_text}\n")

            while True:
                key = input("A key is any string of letters (1-500 chars): ")
                key = clean_text(key)

                if 1 <= len(key) <= 500:
                    break
                else:
                    print("invalid length")
            print(f"Using encryption key: {key}\n")

            final_message = decrypt_text(cipher_text, key)
            print(f"Your message has been decrypted:\n{final_message}\n")
        if primary_input == 3:
            print("\nGenerate an encryption key comprised of random characters (max 500).")

            msg = "Enter the desired length of key: "
            desired_length = validate_input(1, 500, msg, "invalid input", "invalid length")
            key = generate_key(desired_length)
            print(f"Your new encryption key: \n{key}\n")

        if primary_input == 4:
            running = False
            break


if __name__ == "__main__":
    main()