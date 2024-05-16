import os
import signal

"""
signal.SIG_IGN -> ignorar la señal
signal.SIG_DFL -> comportamiento por defecto
funcion(s, f)  -> handler a ejecutar
"""

def manejador_usr1(sig, frame):
    print("Manejando la señal ", sig)
    print("Frame: ", frame)
    
print(os.getpid())

print("Ignoramos la señal USR1")
signal.signal(signal.SIGUSR1, signal.SIG_IGN)
input()

print("Redefinimos la señal USR1: default")
signal.signal(signal.SIGUSR1, signal.SIG_DFL)
input()

print("Redefinimos la señal USR1: handler")
signal.signal(signal.SIGUSR1, manejador_usr1)
input()




#Este código en Python demuestra cómo gestionar señales en un programa. Primero, importa los módulos os y signal.
#
#Luego, define una función de manejador de señal llamada manejador_usr1 que imprimirá información sobre la señal recibida y el marco del proceso.
#
#El programa comienza imprimiendo el ID del proceso utilizando os.getpid().
#
#Luego, muestra un mensaje indicando que se ignorará la señal SIGUSR1 (signal.SIGUSR1) y establece el manejador de señal para SIGUSR1 en signal.SIG_IGN,
#lo que significa que la señal se ignorará si se recibe.
#
#Después de la primera entrada (input()), el programa espera a que el usuario presione Enter antes de continuar.
#
#Luego, el programa redefine el manejo de la señal SIGUSR1 como el comportamiento predeterminado (signal.SIG_DFL). 
#Esto significa que si se recibe la señal SIGUSR1, el programa seguirá el comportamiento predeterminado asociado con esa señal.
#
#Después de la segunda entrada, el programa espera nuevamente a que el usuario presione Enter antes de continuar.
#
#Finalmente, el programa redefine el manejo de la señal SIGUSR1 para que llame a la función manejador_usr1 que hemos definido anteriormente.
#Esto significa que cuando se reciba la señal SIGUSR1, se ejecutará esta función de manejador de señal.
#
#El programa termina después de la tercera entrada.
#
#En resumen, este código ilustra cómo definir diferentes comportamientos para manejar señales en un programa Python.

