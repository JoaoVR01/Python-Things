'''
NASA hires you to analyze a list of asteroids and count how many have a high 
probability of colliding with Earth (those located at a distance less than 4660283 miles). 
NASA provides you with a list of asteroids, which internally contains the name and distance of each asteroid. 
Reuse the following code to count how many asteroids have a high collision probability.
'''

a1 = {"name":"2022 HX1", "distance":1547214} 
a2 = {"name":"2022 HA2", "distance":2870734} 
a3 = {"name":"101955 Bennu", "distance":20188350} 
asteroids = [a1, a2, a3]

asteroid_count = 0
asteroid_namelist = []

for asteroid in asteroids:
    if asteroid["distance"] < 4660283:
        asteroid_count+=1
        asteroid_namelist.append(asteroid["name"])

print("Potential dangerous asteroids:" + str(asteroid_count))
for n in asteroid_namelist:
    print(n)