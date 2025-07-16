from math import sqrt
'''
Faça um programa que receba de um arquivo (entrada.txt) dois pontos e calcule a distância entre eles no plano cartesiano. 
A distância deverá ser exibida na saída padrão.

Sabe-se que dados dois pontos A = (x1,y1) e B = (x2,y2), a distância entre eles é a raiz quadrada da soma das diferenças das coordenadas ao quadrado.
'''

file = open('chapter16ex.txt')
fileContent = file.readlines()

def point_distance(x1, y1, x2, y2):
    dist = sqrt(((x2-x1)**2)+((y2-y1)**2))
    return dist

x1 = float(fileContent[0])
y1 = float(fileContent[1])
x2 = float(fileContent[2])
y2 = float(fileContent[3])

print(f"The distance between the points is: {point_distance(x1,y1,x2,y2):.5f}")
