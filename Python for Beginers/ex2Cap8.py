'''
Your daughter's school needs you to help design a program to determine who won the class representative elections. 
There are two student candidates, and the one with the highest vote count wins. Implement a program that asks the 
user to input the following via keyboard: the name of the first student, the vote count of the first student, the 
name of the second student, and the vote count of the second student. 
The program should print to the screen the name of the winning student (if there is a tie, it should print the message 
"Tie").
'''

name1 = str(input("Enter the candidate name: "))
votes1 = int(input("Enter the amount of votes of this candidate:"))

name2 = str(input("Enter the candidate name: "))
votes2 = int(input("Enter the amount of votes of this candidate:"))

if votes1 > votes2:
    print(f"{name1} wins!")
elif votes2 > votes1:
    print(f"{name2} wins")
else:
    print("Tie")