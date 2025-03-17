def even_odd(num):
    if num % 2 == 0:
        return f"{num} is an even number"
    else:
        return f"{num} is an odd number"

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(even_odd(num))   

input("\n\n\nPress Enter to exit...")