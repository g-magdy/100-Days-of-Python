from constants import Constants
from colorama import Fore, Back, Style

def print_intro():
    print(Fore.CYAN + Constants.INTRO_BANNER + Style.RESET_ALL)
    print(Fore.GREEN + "This program converts text to Morse Code.")
    print("Enter the text to convert to Morse Code.")
    print("The Morse Code will be printed to the console.")
    print("Words will be separated by a forward slash (/) and characters by a space." + Style.RESET_ALL)
    

def validate_input(input_string : str, input_mode: int) -> bool:
    if input_mode == 1:
        # convert from english to morse
        # check that all characters are alphanumeric
        return input_string.isalnum()
    # else, check that the only characters that are in the string are . - /
    for c in input_string:
        if c not in ['.', '-', '/', ' ']:
            return False
    return len(input_string) != 0

def handle_input():
    try:
        mode = int(input(Fore.YELLOW + "Enter 1 to convert text to Morse Code or 2 to convert Morse Code to text: " + Style.RESET_ALL))
        if mode != 1 and mode != 2:
            raise ValueError
    except ValueError:
        print( Fore.RED + "Invalid input. Please enter 1 or 2." + Style.RESET_ALL)
        return handle_input()
    
    if mode == 1:
        input_text = input(Fore.YELLOW + "Enter the text to convert to Morse Code: "+ Style.RESET_ALL)
    else:
        input_text = input(Fore.YELLOW + "Enter the Morse Code you want to convert to text: "+ Style.RESET_ALL)
    
    if validate_input(input_text, mode):
        return input_text, mode
    else:
        print( Fore.RED + "Input is invalid, it is either empty or contains invalid characters")
        if mode == 1:
            print("allowed characters are letters and numbers only"+ Style.RESET_ALL)
        else:
            print("the allowed characters are '.' '-' '/' and space only"+ Style.RESET_ALL)
        return handle_input()


def convert_to_morse_code(input_string):
    morse_code_string = ""
    for char in input_string:
        
        if char.upper() in Constants.morse_code:
            morse_code_string += Constants.morse_code[char.upper()] + " "
        elif char == " ":
            morse_code_string += "/ "
        else:
            morse_code_string += char + " "
            
    return morse_code_string


def convert_to_text(input_string):
    text_string : str = ""
    morse_decode : dict[str, str] = {value: key for key, value in Constants.morse_code.items()}
    words : list[str] = input_string.split(" / ")
    stripped_words : list[str] = [word.strip() for word in words]
    warning_flag = 0
    for word in stripped_words:
        characters = word.split(" ")
        stripped_characters = [c.strip() for c in characters]
        for char in stripped_characters:
            if char not in morse_decode:
                warning_flag = 1
                continue
            text_string += morse_decode[char]
        text_string += " "
    return text_string, warning_flag


def main():
    print_intro()
    input_string, mode  = handle_input()

    if mode == 1:
        morse_code_string = convert_to_morse_code(input_string)
        print(f"The Morse Code for '{input_string}' is:")
        print(morse_code_string)
    else:
        text_string, warning_flag = convert_to_text(input_string)
        print(f"The text obtained from '{input_string}' is:")
        print(text_string) 
        print("SKIPPED Invalid Characters!" if warning_flag else "All characters have been found")
        

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye bro, have a good day")