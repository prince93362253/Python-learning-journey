def odd_number_printer(n):
    j = 1
    for i in range (1, n+1):
        if i%2 != 0:
            print(f"Number {j} = {i}")
            j += 1

def odd_number_printer_2(n):
    for index, numbers in enumerate(range(1, n+1, 2), start=1):
            print(f"Number {index} = {numbers}")
    


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    odd_number_printer(n)
    odd_number_printer_2(n)