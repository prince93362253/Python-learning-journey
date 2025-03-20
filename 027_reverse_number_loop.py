def reverse_loop(n):
    for i in range(n, -1):
        print(i)

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    reverse_loop(n)