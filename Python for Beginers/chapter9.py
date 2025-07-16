'''
while loop

i = 0
while i < 3:
    print(i)
    i += 1
print("End program")
'''
#print yhe multiples of 5, from 5 to 25
'''
i = 1
top = 25
counter = 5
while counter <= top:
    print(counter)
    counter = 5*i
    i += 1

#arithmetic progression
'''
'''
an = a1 + r(n-1)
r = common difference
an = last term
n = number of terms
a1 = first term
'''
'''
a1 = float(input("Enter the first term: "))
r = float(input("Enter the common difference: "))
n = int(input("Enter the number of terms: "))

i = 1
while i <= n:
    print(a1 + r*(i - 1)) 
    i += 1
''' 
i = 5
while i <= 25:
    print(i)
    i += 5   
print("-------------------------------")
i = 10
while i >= 0:
    print(i)
    i -= 1
print("-------------------------------")
num = int(input("Enter the number of times you want yo print: "))
i = 0
while i < num:
    print("Python is fun!")
    i += 1