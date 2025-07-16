#boolean vareable = type bool
#store true or false values
'''
age = True
print(type(age))
print(age)
'''
'''
Operators:
== Equal to
!= Not equal to 
< Less than 
> Greater than 
<= Less than or equal to 
>= Greater than or equal to

Logical operators:
and - operator evaluates to True if both Boolean values (or expressions) are true. 
      Otherwise, it evaluates to False.

or - evaluates the comparison to True if either Boolean value (or expression) is true. 
     Only if both are false does it evaluate to False.
     
not - evaluates to the opposite value of the Boolean value of the expression. 
'''
'''
name = "Ana"
age = 17

result = bool(name == "Ana" and age > 15)
print(result)
'''

temp = float(input("Enter the current temperature outside: "))
money = float(input("Enter the amount of cash: "))


if temp > 27 and money >= 5:
      print("Buy ice cream!")

print("End of program")
#conditional if: change the program natural flow
#the "if action" will only be executed if the condition is true
#the identation is very important!!!!