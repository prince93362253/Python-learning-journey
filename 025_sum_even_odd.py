n = int(input("Enter the number: "))

even_number_sum = 0
odd_number_sum = 0

for index, number in enumerate(range(1, n+1), start=1):
    if number % 2 == 0:
        even_number_sum += number
    else:
        odd_number_sum += number

print("Sum of even numbers:", even_number_sum)
print("Sum of odd numbers:", odd_number_sum)
