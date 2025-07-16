'''
A philologist (a person who studies languages) is conducting a research to communicate with aliens. 
We all know that aliens do not use vowels. Therefore, the philologist wants to have a program that, 
when given a word, shows each letter of that word on a separate line. And if any letter corresponds to a vowel, 
do not show it. Write a program that asks the user to enter a word through the keyboard. 
Then, print each character of the word on a separate line (excluding the characters that represent vowels).
'''

text = input("Enter a text: ")
txt = text.upper()
i = 0
while i < len(txt):
    if txt[i] != "A" and txt[i] != "E" and txt[i] != "I" and txt[i] != "O" and txt[i] != "U":
        print(text[i])
    i+=1