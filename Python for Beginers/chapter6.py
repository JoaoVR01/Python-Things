#the input function: get the keyboard input until the user press enter

name = str(input("Type your name: \n")) #str function is used to chage the data type
print(f"Hi {name}. Nice to meet you!")

#int and float functions works like the str function
age = int(input("Enter your age: \n"))
halfAge = age/2 
print(f"Your half age is {halfAge}.")

#Concatenation
name_2 = "Thales"
age_2 = 24

print("Name: " + name_2)
print("Age: " + str(age_2))
#str function is used because Python cant concatenate text with numbers
#we can use , to separate the variables in the print

print("List of ages: ",age,",",age_2,".")
print("List of names: ",name,",",name_2,".")