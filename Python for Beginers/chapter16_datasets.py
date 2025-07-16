#top 10 music
file = open("songs.csv", encoding="utf-8")
fileContent = file.readlines()

i = 1
print("Top 10 songs: \n")
while(i < 11):
    line = fileContent[i].strip().split(",")
    print(line[1])
    i+=1
print("---------------------------------------------------")
#top 10 artists
singer_list = []
#create a list with all the singers(with copies)
for line in fileContent:
    line = line.strip().split(",")
    singer_list.append(line[0])
    
#create a list with dictionaries that contain the the name of the artist and how many times it appear
the_most_list = []
for singer in singer_list:
    the_most_dict = {"artist": singer, "count": singer_list.count(singer)}
    the_most_list.append(the_most_dict)
    if the_most_list.count(the_most_dict) != 1:#here we eliminate the repeated dictionaries
        the_most_list.remove(the_most_dict)
    
the_most_list = sorted(the_most_list, key=lambda d: d["count"], reverse=True)
#here we sorted the list with the "count" key from the largest to smallest
print("Top 10 artists: \n")
j = 0
while j < 10:
    print(the_most_list[j]["artist"]+" "+str(the_most_list[j]["count"])+" times")
    j += 1