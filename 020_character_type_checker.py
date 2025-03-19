def check_character(character):
    if character.isalpha():
        if character.isupper():
            print(f"{character} is an uppercase letter.")
        else:
            print(f"{character} is a lowercase letter.")
    elif character.isdigit():
        print(f"{character} is a digit.")
    else:
        print(f"{character} is a special character.")

if __name__ == "__main__":
    character = input("Enter the character: ")
    character = character[0]
    check_character(character)

input("Press enter to continue...")