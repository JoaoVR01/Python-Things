'''
A tsunami monitoring station needs a system to issue alerts. 
The station must issue an alert when an earthquake of magnitude 5.2 or greater occurs. 
Implement a program that asks the user to enter the magnitude of an earthquake by the keyboard. 
If the entered magnitude is greater than or equal to 5.2, print "Tsunami alert!!".
'''

earthquake = float(input("Enter the magnitude of the earthquake:"))

if earthquake >= 5.2:
    print("Tsunami alert!!")
print("Relax.")