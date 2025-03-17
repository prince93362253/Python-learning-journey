def mul_table(n):
    for i in range(1, 10):
        multipy=n*i
        print(f"{n} * {i} = {multipy}")

if __name__=="__main__":
    n=int(input("Enter the number: "))
    mul_table(n)

input("\n\n\nPress Enter to exit...")