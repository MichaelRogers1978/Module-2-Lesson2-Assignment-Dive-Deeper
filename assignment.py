#task 1.1

number = int(input("Enter a number:"))
if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negitive.")


#task 2.1

users_number_one = int(input ("number 1: "))
users_number_two = int(input ("number 2: "))
users_number_three = int(input ("number 3: "))
if users_number_one <= users_number_two and users_number_one <= users_number_three:
    print(f"The smallest number is {users_number_one}")
elif users_number_two <= users_number_three and users_number_two <= users_number_one:
    print(f"The smallest number is {users_number_two}")
elif users_number_three <= users_number_one and users_number_three <= users_number_two:
    print(f"The smallest number is {users_number_three}")

if users_number_one >= users_number_two and users_number_one >= users_number_three:
    print(f"The largest number is {users_number_one}")
elif users_number_two >= users_number_three and users_number_two >= users_number_one:
    print(f"The largest number is {users_number_two}")
elif users_number_three >= users_number_one and users_number_three >= users_number_two:
    print(f"The largest number is {users_number_three}")