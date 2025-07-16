'''
A crazy scientist always miscalculates the years when an asteroid will likely fall to Earth. 
If the scientist says that an asteroid will fall in 10 years, it's because it will fall in 5 years 
(he always overestimates the actual number of years by double). 
Write a program that asks the user to enter the number of years until an asteroid falls 
(according to the crazy scientist, in float format). Then, print the text “The asteroid 
will fall in:”, concatenate it with the actual result of the years until it falls, and finally, 
concatenate it with the text “years”.
'''

years = float(input("Years until an asteroid falls: "))
result = years/2

#way 1:
print("The asteroid will fall in: " + str(result) + " " + "years.")

#way 2:
print(f"The asteroid will fall in: {result} years.")