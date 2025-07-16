'''
Write a program that asks the user to enter an integer number through the keyboard. 
This number will represent the number of soccer teams the user is a fan of. Then, 
create an empty list called teams. Create a loop that will iterate as many times as the
number entered by the user (for example, if the user enters 3, a loop that runs 3 times should be created). 
Now, inside the body of the loop, ask the user to enter the name and country of a team through the keyboard. 
Then create a dictionary with keys "name" and "country", and associate the values received from the keyboard 
with those keys. Before the loop body ends, add the dictionary to teams. Finally, outside the loop, print the teams list.
'''

number = int(input("Enter a number: "))
team_list = []
i = 0
while i < number:
    teamName = str(input("Enter a team name: "))
    teamCountry = str(input("Enter the team country: "))
    teamInfo = {'name': teamName, 'country': teamCountry}
    team_list.append(teamInfo)
    i+=1
print(team_list)