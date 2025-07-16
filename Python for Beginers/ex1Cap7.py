'''
Write a program that asks the user to enter the distance in miles at which their partner is located (who is home alone). 
If the entered distance is less than or equal to 4, print “I am coming over”.
'''

distance = float(input("Enter the distance in miles: "))

if distance <= 4:
    print("I'm coming over")
print("End program")