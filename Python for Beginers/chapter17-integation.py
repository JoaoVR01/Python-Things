import matplotlib.pyplot as ptl

fileCsv = open("songs.csv", encoding="utf-8")
contentCsv = fileCsv.readlines()
i = 0
data_list = []
duration_list = []
year_list = []

#read the duration(ms) of the musics and the year:
while i < len(contentCsv):
    line = contentCsv[i].strip().split(",")
    duration_dict = {"duration":line[2],"year":line[4]}
    data_list.append(duration_dict)
    i+=1

#sorting the list:
data_list = sorted(data_list, key=lambda d: d["year"])
aux = data_list[0]
max_list = []

aux_year = data_list[0]["year"]
max_duration = int(data_list[0]["duration"])

for item in data_list:
    year = item["year"]
    try:
        duration = int(item["duration"])
    except ValueError:
        continue  # ignora valores inválidos

    if year == aux_year:
        if duration > max_duration:
            max_duration = duration
    else:
        # Adiciona o dicionário com o ano e a duração máxima encontrada até agora
        max_list.append({"year": aux_year, "max_duration": max_duration})
        aux_year = year
        max_duration = duration

# Adiciona o último ano após o loop
max_list.append({"year": aux_year, "max_duration": max_duration})

for item in max_list:
    year_list.append(item["year"])
    duration_list.append(item["max_duration"])
    
ptl.plot(year_list, duration_list)
ptl.xlabel("Duration (ms)")
ptl.ylabel("Year")
ptl.show()