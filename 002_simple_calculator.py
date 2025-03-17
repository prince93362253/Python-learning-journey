def sim_calc(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    # division = num1 / num2
    print(f"The sum of {num1} and {num2} is {addition}")
    print(f"The difference of {num1} and {num2} is {subtraction}")
    print(f"The product of {num1} and {num2} is {multiplication}")

    if num2 == 0:
        print("Division by zero is not possible")
    else:
        division = num1 / num2
        print(f"The quotient of {num1} and {num2} is {round(division,2)}")

if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    sim_calc(num1, num2)

input("\n\n\nPress Enter to exit...")