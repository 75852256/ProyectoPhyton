#Problema 2: halle el volumen de un cilindro
import math
rad = float(input("Poner el radio:"))
h = float(input("Poner altura:"))
#π r² h
area = math.pi * math.pow(rad, 2) * h
print("El producto de sus digitos es: ", area)
