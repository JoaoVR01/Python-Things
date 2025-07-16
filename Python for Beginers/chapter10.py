message = "Hello, world!"

print(len(message))
#this is how we know the length of a string

print(message[4])
#this is how we extract a character of a string

print(message[0:5])
#this is how we extract a substring of a string

print(message[::-1])
#this is how we invert a string in python

print(message*3)
#repeat the string 3 times

'''
Arithmetic operators:
+ Add
- Subtract
* Multiplication
/ Division
** Expontial
// Int division
% Remainder of division
'''

print(message.count("l"))
#how many times some character apears

print(message.find("l"))
#show the first index of a character in the string
#show -1 if the string doesn't have the charcter

if "Hello" in message:
    print("Yes")
#the operator in is used in conditions with substings or characters

print(message.lower())
#returns the lowercased string

print(message.upper())
#returns the uppercased string

print(message.replace("Hello", "Hola"))
#returns the string replacing "Hello" by "Hola"

print(message.capitalize())
#returns the string with the first character uppercased and the others lowercased

print(message.title())
#returns the string with the first character of each word uppercased

print(message.strip())
#returns the string without any blank spaces at the beginning or at the end

