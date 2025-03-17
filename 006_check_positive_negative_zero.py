def check_num_sign(num):
    if num > 0:
        return f"{num} is a positive number"
    elif num < 0:
        return f"{num} is a negative number"
    else:
        return "Zero"
    
if __name__=="__main__":
    num = int(input("Enter a Number: "))
    print(check_num_sign(num))

input("\n\n\nPress Enter to exit...")