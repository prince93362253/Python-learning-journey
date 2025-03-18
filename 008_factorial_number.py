# 007_factorial_number.py

def factorial(n):
    if n < 0:
        return "Enter a valid non-negative number."
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print(f"Factorial of {n} is {factorial(n)}")
