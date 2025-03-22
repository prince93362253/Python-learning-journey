my_list = [10, 20, 4, 45, 99, 99, 33]
new_list = sorted(set(my_list),reverse=True)
if len(new_list) > 1:
    print(f"The second largest number in the list is {new_list[1]}")
else:
    print(f"Enter the correct list") 