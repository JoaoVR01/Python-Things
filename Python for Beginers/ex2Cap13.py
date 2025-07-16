'''
A woman is looking for a name for her baby boy. A friend sends her a list of options with the following names: 
"Lucas", "David", "Logan" and "Mike". However, the woman has had bad experiences with men whose names start with 
"L". Write a program that asks the user to enter the four names. Then, add the four names to a list, and iterate 
over the list of names using a for loop. Inside the loop, check whether the name being iterated starts with the 
letter "L". If so, print a message "Name discarded". If not, print a message "Possible name". Hint: 
remember how to extract a character from a string.
'''

name_list = ["Lucas", "David", "Logan", "Mike"]

for name in name_list:
    if name[0].lower() == 'l':
        print(f"{name} - Name discarted")
    else:
        print(f"{name} - Possible name")
        