#this is how we use a counter
'''
number_list = [12,3,4,5,6,12,5,6,7,8,12,12,12,3,4,5,12]
counter = 0
for n in number_list:
    if n == 12:
        counter+=1
print(counter)
'''

#voting system counter aplication
print('There are 3 candidater: 14, 21, 55')

def apuration(vote_list):
    valid_votes = 0
    name_list = []
    
    for n in vote_list:
        name_list.append(n['name']) 
    for vote in vote_list:
        if vote['number'] in [14,21,55] and vote['name'] != '' and name_list.count(vote['name']) == 1:
            valid_votes += 1
    return valid_votes

vote_list = []

while True:
    name = str(input("Enter your name: "))
    if name.lower() == 'exit':
        break
    candidate_number = int(input("Enter the candidate number: "))
    vote = {'name':name, 'number':candidate_number}
    print(vote)
    vote_list.append(vote)
    
    
valid_votes = apuration(vote_list)

print(f"Number of valid votes: {valid_votes}")
    