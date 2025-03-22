my_string = input("Enter the string\n")
result = ""
for i in range(0, len(my_string)):
    if i%2 == 0:
        result += my_string[i].upper()
    else:
        result += my_string[i].lower()
print(result)