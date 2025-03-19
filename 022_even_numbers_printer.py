def even_number_print(n):
    if n > 0:
        j = 1
        for i in range (1, n+1):
            if i % 2 == 0:
                print(f"Number {j} = {i}")
                j += 1

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    even_number_print(n)

input("Press enter to continue...")