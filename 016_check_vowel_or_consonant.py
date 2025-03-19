def check_alphabet(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if alphabet.isalpha():
        if alphabet.lower() in vowels:
            print("This is a vowel")
        else:
            print("This is a consonant")
    else:
        print("This is not an alphabet")

if __name__ == "__main__":
    alphabet = input("Enter an alphabet: ")
    check_alphabet(alphabet)    

input("Press Enter to continue...")
        