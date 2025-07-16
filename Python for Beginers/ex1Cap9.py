'''
Write a program that asks the user to enter a number via keyboard input. 
Then, create a loop that repeats as many times as the entered number 
(for example, if the user enters 3, the loop should run three times). 
And then, within the body of loop, print four asterisks "****". 
'''

num = int(input("Enter the number of times the loop will repeat: "))
i = 0
while i < num:
    print("****")
    i += 1
