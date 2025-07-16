def add():
    numbers = list(map(float, input('Enter two numbers: ').split()))
    print(numbers[0] + numbers[1])

def sub():
    numbers = list(map(float, input('Enter two numbers: ').split()))
    print(numbers[0] - numbers[1])

def div():
    numbers = list(map(float, input('Enter two numbers: ').split()))
    if numbers[1] != 0:
        print(numbers[0] / numbers[1])
    else:
        print('Math error!')
        
def mult():
    numbers = list(map(float, input('Enter two numbers: ').split()))
    print(numbers[0] * numbers[1])
    
def square():
    number = float('Enter a nume]ber:')
    print(number**2)
    
while True:
    print('Enter the operation: ')
    print('1)Add \n2)Subtraction \n3)Division \n4)Multiplication \n5)Square \n0) Exit')
    operation = int(input())
    if operation == 0:
        break
    elif operation == 1:
        add()
    elif operation == 2:
        sub()
    elif operation == 3:
        div()
    elif operation == 4:
        mult()
    elif operation == 5:
        square()