import random

def input_validifyer() -> int:
    """Validifies the input by first making sure it's a number and then checks
    if it is between 1 and 4 inclusive."""

    validity = False

    print("""Please choose from one of the following menu options:
1. Encrypt plaintext.
2. Decrypt ciphertext.
3. Generate key.
4. Exit.""")
    while validity == False:
        while True:    
            try:
                primary_input = int(input(">"))
                break
            except ValueError:
                print("invalid input")
        if 1 <= primary_input <= 4:
            validity = True
        else:
            print("Invalid choice. Try again.")
            validity = False
    return(primary_input)


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


    spacer = 5
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    playing = True

    while playing == True:
        final_message = ""
        print("""----------------------------------
EasyCrypt Text Encryptor/Decryptor
----------------------------------""")
        primary_input = input_validifyer()
        if primary_input == 1:
            plain_text_encryptor(spacer, ALPHABET, final_message)
        #if primary_input == 2:
        
        #if primary_input == 3:
        
        #if primary_input == 4:
            playing = False
            break


if __name__ == "__main__":
    main()