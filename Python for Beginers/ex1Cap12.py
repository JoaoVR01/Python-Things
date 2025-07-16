'''
Implement a program in which you ask the user to enter the name, age, and gender of a pet through the keyboard. 
Then create a dictionary with three keys: "name", "age", and "gender", and associate each of the values received 
from the keyboard with those keys. Finally, print the dictionary.
'''

name = str(input("Enter the name of the pet: "))
age = int(input("Enter the age of the pet: "))
gender = str(input("Enter the gender of the pet: "))

pet_info = {'name': name, 'age': age, 'gender': gender}

print(pet_info)