def check_number(number):
    if number > 0:
        print(f"{number} is a positive number")
    elif number == 0:
        print(f"{number} is zero")
    else:
        print(f"{number} is a negative number")

if __name__ == "__main__":  
    number = int(input("Enter the number to check: "))
    check_number(number)

input("\n\n\nPress Enter to exit...")