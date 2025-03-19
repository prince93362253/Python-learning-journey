def grade_checker(marks):
    if 0 <= marks <= 100:
        if 90 <= marks <= 100:
            print("Your grade is A+")
        elif 80 <= marks <= 89:
            print("Your grade is A")
        elif    70 <= marks <= 79:
            print("Your grade is B")
        elif 60 <= marks <= 69:
            print("Your grade is C")
        elif 50 <= marks <= 59:
            print("Your grade is D")
        elif 50 > marks:
            print("Fail")
        else:
            print("Enter the correct marks")
    else:
        print("Enter valid marks")

if __name__ == "__main__":
    marks = int(input("Enter your marks: "))
    grade_checker(marks)