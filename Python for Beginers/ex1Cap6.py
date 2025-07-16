'''
Write a program that asks the user to input their first name, last name, age, 
and height. Store each value in a separate variable (you will have four variables). 
Finally, print the contents and type of each variable. 
Note: when requesting input from the user, convert the values to the most appropriate types.
'''

first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your last name: "))
age = int(input("Enter your age: "))
height = float(input("Enter your height:  "))

print(first_name + str((type(first_name))))
print(last_name + str((type(last_name))))
print(str(age) + str((type(age))))
print(str(height) + str((type(height))))