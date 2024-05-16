"""Este código en Python establece un manejador de señal para la señal SIGALRM que imprime un mensaje cuando se activa.
Luego, configura una alarma para que suene después de 5 segundos utilizando signal.alarm(5). 
Después de establecer la alarma, el programa imprime "Después de alarm y antes de pause" y luego entra en un estado de espera hasta que se recibe una señal.

La función signal.pause() suspende el programa hasta que se recibe una señal.
En este caso, el programa espera hasta que la alarma SIGALRM se activa después de 5 segundos. 
Una vez que la señal de alarma se recibe, se llama al manejador handler y se imprime el mensaje correspondiente.

Finalmente, después de que el manejador de señal maneje la alarma, el programa imprime "Después de pause" y desactiva la alarma con signal.alarm(0).

En resumen, este código crea una pausa en la ejecución del programa durante 5 segundos antes de que se active una señal de alarma, 
y luego continúa su ejecución después de manejar la señal de alarma.
"""

import os, signal
import time

def handler(s, f):
    print('Se ha llamado al manejador')
    # print(f)

def main():
    signal.signal(signal.SIGALRM, handler)

    print("Antes de alarm")
    signal.alarm(5)
    print("Después de alarm y antes de pausa")
    signal.pause()
    # time.sleep(10)
    print("Después de pausa")

    signal.alarm(0)  #Deshabilita la alarma
    print("Después de deshabilitar la alarma")
    
    
if __name__ == '__main__':
    main()


    