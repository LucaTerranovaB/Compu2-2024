#!/usr/bin /python3

import sys

class Ejercicio2():

    def __init__(self):
        self.args = sys.argv
        self.cadena = self.args[1]
        self.numero = int(self.args[2])

    #Verificar si se ingresaron los 2 argumentos requeridos
    def VerificarArgumentos(self,args):
        if len(args) !=3 :
            print("Error!! Se requieren dos argumentos: una cadena de texto y un numero entero")
            sys.exit(1)
        else:
            print("Argumentos ingresados correctamente")
    
    #Obtener la cadena de texto y el numero entero
    def ObtenerArgumentos(self,cadena,numero):
        cadena = self.cadena
        numero = self.numero

    #Imprimir la cadena de texto n veces
    def ImprimirCadena(self,cadena,numero):
        print(cadena*numero)


if __name__ == "__main__":
    Ejercicio2().VerificarArgumentos(Ejercicio2().args)
    Ejercicio2().ObtenerArgumentos(Ejercicio2().cadena,Ejercicio2().numero)
    Ejercicio2().ImprimirCadena(Ejercicio2().cadena,Ejercicio2().numero)

    