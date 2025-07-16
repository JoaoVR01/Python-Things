#accumulators
'''
salaries = [3000,5000,1500]
acumulator = 0
for n in salaries:
    acumulator+=n
print(acumulator)
'''

cities = [{'name':'Divinópolis','population':250000},
          {'name':'Lavras','population':105000},
          {'name':'Belo Horizonte','population':2000000}]
acumulator = 0
for city in cities:
    acumulator += city['population']
print("Total population: " + str(acumulator))
print("Average ppopulation: " + str(acumulator/len(cities)))

print('------------------------------------------')

#flags
# a boolean variable that checks if a certain situation has occourred
#example

grades = [1.0, 3.5, 4.0, 4.7, 0.6]

flag = False
for grade in grades:
    if grade > 4.5:
        flag = True
        break

if flag:
    print("You obtained at least one high grade")
else:
    print("You did not obtained high grades")