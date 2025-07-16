#functions

# A function is a block of code designed to perform a specific task.

'''
function body:
def function_name(parameters):
    instructions
'''

def greet():
    print("Welcome")
    print('To my program')

greet()

def add(num1, num2):
    result = num1 + num2
    print(result)

add(3,5)

#global and local scope
#variables or parameters created or defined inside a function only exists in a local scope
#example:
'''
    def add(n1+n2):
        result = n1+n2
        print(result)
    add()
    print(result) => it would be a error cause result only exists inside add function
'''

#variables defined outside any function exists in a global scope and can be accessed anywhere in code
#example:
'''
def totalprice(price)
    total = price + tax
    print(total)
    
tax = 10
toralprice(100) => it is right cause tax is a globaal variable
'''