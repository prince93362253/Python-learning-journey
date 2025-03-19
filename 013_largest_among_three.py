def check_largest(num1, num2, num3):
    if num1==num2==num3:
        return "All numbers are equal"
    elif num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3
    
if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    print("Largest number is : ", check_largest(num1, num2, num3))

input("Press Enter to continue...")