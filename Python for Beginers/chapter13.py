#for loop 

#a for loop executes a set of instructions for each element in a sequence.

#for loop with lists
ages = [23, 4, 56, 7]
for age in ages:
    print(age)
print('----------------------------')
#for loop with strings
message = 'Hello, world!'
for character in message:
    print(character)
print('----------------------------')    
#for loop with dictionaries
personal_info = {'name': 'pablo', 'last name':'silva', 'team': 'cruzeiro'}
for key in personal_info:
    print(f'{key}: {personal_info[key]}')
print('----------------------------')
#range funciton

#with a single argument: range(stop)
for i in range(6):
    print(i)
    #the sequance starts with 0. the stop number isn't included
print('----------------------------')
#with two arguments: range(start, stop)
for i in range(3,10):
    print(i)

print('----------------------------')
#with three arguments: range(start, stop, step)
for i in range(1,10,2):
    print(i)
print('----------------------------')   
# when you put a negative number in the step, you make a inverted sequence
for i in range(10,0,-1):
    print(i)