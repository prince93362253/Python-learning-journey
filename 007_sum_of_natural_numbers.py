# sum of natural numbers

def total_of_n(n):
    if n > 0:
        total = 0
        for i in range(1, n+1):
            total += i
        return total
        # print(f"Sum of first {n} natural numbers is {total}")
    else:
        print(f"Enter the correct natural Number")

if __name__=="__main__":
    n = int(input("Enter the natural number: "))
    total = total_of_n(n)
    print(f"Sum of first {n} natural numbers is {total}")
    
input("\n\n\nPress Enter to exit...")