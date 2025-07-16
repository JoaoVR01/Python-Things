'''
Write a program that asks the user to enter a text via keyboard. 
Then, print the first character of that text concatenated with the last character.
'''

text = input("Enter a text: ")
firstChar = text[0]
lastChar = text[len(text) - 1]
print(firstChar + lastChar)