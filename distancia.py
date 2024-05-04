"""
Hacer un programa que encuentre la distancia entre dos puntos
"""
import numpy as np 
while True:
    def distancia(p1,p2):
        distX = p1[0] - p2[0]
        distY = p1[1] - p2[1]
        distTotal = np.sqrt(distX**2 + distY**2)
        return distTotal
    print("===Bienvenido a un programa que calcula la distancia entre dos puntos===")
    primer_p = int(input("Ingresa un numero entero para el que le quieras calcular la distancia:"))
    segundo_p = int(input("Ingresa un numero entero para el que le quieras calcular la distancia:"))
    tercer_p = int(input("Ingresa un numero entero para el que le quieras calcular la distancia:"))
    cuarto_p = int(input("Ingresa un numero entero para el que le quieras calcular la distancia:"))
    print("La distancia para los numeros que ingresastes es:",distancia([primer_p,segundo_p],[tercer_p,cuarto_p]))
    pregunta = input("Quieres salir del programa:")
    if pregunta == "si":
        break
    #Se podria hacer una gráfica de estos dos puntos#
