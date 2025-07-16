'''
Some aliens from another galaxy left a secret message in a Python code snippet shown below:
secretMessage = ["Planet", "You", "Secret", "Are", "Zombie", "The", "Nuclear", "Alien"] 
Now we need to decipher that message. To do that, take the previous list, and then iterate 
through the list with a loop and print to the screen only the values stored in the odd indexes 
of the list (i.e., 1, 3, 5, and 7).
'''

secretMessage = ["Planet", "You", "Secret", "Are", "Zombie", "The", "Nuclear", "Alien"]
i = 1
while i < len(secretMessage):
    print(secretMessage[i])
    i += 2
