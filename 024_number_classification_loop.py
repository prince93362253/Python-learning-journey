def number_classification_loop(n):
    for index, number in enumerate(range(1, n+1), start = 1):
        if number%2 == 0:
            print(f"{number} - Even Number")
        else:
            print(f"{number} - Odd Number")

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    number_classification_loop(n) 