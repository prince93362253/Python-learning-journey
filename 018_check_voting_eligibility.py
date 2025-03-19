def check_voting_eligibility(age):
    if age < 0:
        return "Invalid age entered"
    elif age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

if __name__ == "__main__":
    age = int(input("Enter the age: "))
    print(check_voting_eligibility(age))

    input("Press Enter to continue...")