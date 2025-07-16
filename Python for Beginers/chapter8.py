'''
side = float(input("Enter the side of the square: "))

if side <= 0:
    print("ERROR!")
else:
    area = pow(side, 2)
    print(f"The area of the square is: {area:,.5f}") 
    #this is how we limit or increase the number of decimal cases in python

print("End program")
'''

#vacination stage with elif
'''
age = int(input("Enter your age: "))

if age >= 70:
    print("Stage 1")
elif age >= 60 and age < 70:
    print("Stage 2")
elif age >= 30 and age < 60:
    print("Stage 3")
else:
    print("Stage 4")
    
print("Vacine is good!")
#the condition in elif will only be evalueted if the previous was False
'''

#nested conditionals

option = int(input("Enter the attraction number: "))

if option == 1:
    height = float(input("Enter your height: "))
    if height >= 121.92:
        print("Enjoy the roller coaster!")
    else:
        print("Height not allowed!")
elif option == 2:
    print("Enjoy the train ride!")
else:
    print("Not an attraction number!")
print("End program")