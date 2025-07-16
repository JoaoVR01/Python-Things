'''
Write a program that displays the average popularity of all songs.
'''

fileCsv = open("songs.csv", encoding="utf-8")
contentCsv = fileCsv.readlines()

popularity_sum = 0
i = 1
while i < len(contentCsv):
    line = contentCsv[i].strip().split(",")
    popularity_sum += int(line[5])
    i+=1

average = popularity_sum/2000
print(f"The popularity average is {average}")   
