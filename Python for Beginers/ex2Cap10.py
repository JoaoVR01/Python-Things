'''
A librarian has to analyze texts from different books. 
But the librarian hates analyzing texts that contain the letter “z”. 
The librarian asks you to develop a program that informs her if a text contains any letter “z”. 
Write a program that asks the user to enter a text through the keyboard. 
Then, if the text contains at least one letter “z”, print “Text contains letter z” on the screen. 
Otherwise, print “Text does not contain letter z”. 
Hint: for this exercise, you can use count or find. If you use find, remember that the find method returns -1 
if it does not find a character or substring within a text.
'''

text = input("Enter a text: ")
txt = text.lower()
if txt.find("z") == -1:
    print("Text does not contain letter z")
else:
    print("Text contains letter z")
    