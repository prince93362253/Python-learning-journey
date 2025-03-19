def n_numbers(n):
    for i in range(1, n+1):
        print(f"Number {i} = {i}")

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    n_numbers(n)

input("Press enter to continue...")