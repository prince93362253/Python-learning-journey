def is_palindrome(string):
    reversed_str = string[::-1]
    if string == reversed_str:
        print(f"Yes the string is a palindrome string...")
    else:
        print("No the string is not a palindrome string")

if __name__ == "__main__":
    string = input(f"Enter the string to check the palindrome: ")
    is_palindrome(string)

input("\n\n\nPress Enter to exit...")