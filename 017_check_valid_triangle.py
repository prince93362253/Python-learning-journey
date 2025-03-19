def check_triangle(a, b, c):
    if a+b+c == 180 and a>0 and b>0 and c>0:
        print("This is a valid triangle")
    else:
        print("This is not a valid triangle")       

if __name__ == "__main__":
    a = int(input("Enter the first angle: "))
    b = int(input("Enter the second angle: "))
    c = int(input("Enter the third angle: "))
    check_triangle(a, b, c)

input("Press Enter to continue...")