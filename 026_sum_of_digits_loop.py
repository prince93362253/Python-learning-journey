def sum_of_digits(n):
    sum_of_numbers = 0
    for i in str(n):  # Convert number to string to iterate over digits
        sum_of_numbers += int(i)  # Convert digit back to int and add
    print(f"Sum of digits: {sum_of_numbers}")

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    sum_of_digits(n)
