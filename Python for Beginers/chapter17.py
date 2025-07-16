#libraries

#math library
import math as m

#square root program
number = int(input("Enter a number: "))
if number < 0:
    print(f"{number} does not have real square root")
else:
    sqrt = m.sqrt(number)
print(f"{sqrt:.3f}")

#random library
import random as r

#draw program
name_list = []
sentinel = True
while sentinel:
    name = str(input("Enter a nikcname: "))
    if name.lower() == "0":
        sentinel = False
    else:
        name_list.append(name)
winner = r.choice(name_list)
print(f"The winner is {winner}")

