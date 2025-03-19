# 015_check_divisibility.py
def check_divisibility(number, divisor):
    if divisor == 0:
        return "Error: Division by zero is not allowed."
    return number % divisor == 0

if __name__ == "__main__":
    number = int(input("Enter the first number: "))
    divisor = int(input("Enter the second number (divisor): "))
    
    if divisor == 0:
        print("Error: Division by zero is not allowed.")
    elif check_divisibility(number, divisor):
        print(f"{number} is divisible by {divisor}.")
    else:
        print(f"{number} is not divisible by {divisor}.")

input("Press Enter to continue...")
