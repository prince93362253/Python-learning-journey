def square_root(num):
    if num < 0:
        print("Square root of negative numbers is not supported.")
    else:
        square_root = num**(1/2)
        print(f"The square root of {num} is {round(square_root, 2)}")

if __name__=="__main__":
    num=int(input("Enter the number: "))
    square_root(num)

input("\n\n\nPress Enter to exit...")