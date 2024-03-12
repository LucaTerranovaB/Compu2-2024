# 1-Escribir un programa que acepte un numero de argumento entero positivo n y genere una lista de los n primeros números impares.
# El programa debe imprimir la lista resultante en la salida estandar.

#!/bin/bash python3


import sys
import os

#Obtener los argumentos de la linea de comandos
class Ejercicio1():

    def __init__(self):

        self.args = sys.argv
        self.n = int(self.args[2]) #Numero de argumentos que se pasan por consola

    def listaImpares(self,n):

        #Generamos la lista de numeros impares
        listaI = [i for i in range(n*2) if i%2 != 0]
        print(listaI,  "Numeros impares")

    def listaPares(self,n):

        #Generamos lista de numero pares
        listaP = [i for i in range(n*2) if i%2 == 0]
        print(listaP,  "Numeros pares")

if __name__ == "__main__":
    
        Ejercicio1().listaImpares(Ejercicio1().n)
        Ejercicio1().listaPares(Ejercicio1().n)

        
