'''
Imagine that you are creating a system access mechanism that requires users to enter a specific keyword. 
Write a program with an infinite loop. Then, within the body of the loop, ask the user to enter a word 
via keyboard input. If the entered word is not "Robert", the program should print the "Incorrect keyword" 
message, and the loop will repeat. However, if the entered word is "Robert", the program should print 
"Correct keyword" and stop the loop with a break statement.
'''
while True:
    keyword = input("Enter the keyword: ")
    if keyword != "Robert":
        print("Incorrect keyword")
    else:
        print("Correct keyword")
        break