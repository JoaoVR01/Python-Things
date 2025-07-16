'''
Write a program that asks the user to enter their first name and last name via keyboard input. 
The program should print the last name, followed by a space, and then the first name, all on 
the same line. 
Hint: to insert a space in between, concatenate the last name with “ ” and then concatenate 
the first name.

'''

first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your last name: "))

#way 1:
print(last_name + " " + first_name)

#way 2:
print(f"{last_name} {first_name}")