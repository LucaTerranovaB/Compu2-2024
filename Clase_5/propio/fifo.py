"""
    Este código en Python crea un pipe con un nombre (pipe_name) en el sistema de archivos temporal (/tmp). Luego, crea un proceso hijo que escribe en el pipe, mientras que el proceso padre lee desde él.

Aquí está el flujo del programa:

    Se importan los módulos os y time.
    Se define una función child_v2() que es ejecutada por el proceso hijo. En esta función, se abre el pipe para escritura ('w'), y luego en un bucle infinito escribe en el pipe un mensaje que contiene un número incrementado, duerme durante un segundo y repite el proceso. El método flush() asegura que los datos escritos se envíen inmediatamente al pipe.
    Se define una función parent() que es ejecutada por el proceso padre. En esta función, se abre el pipe para lectura ('r'), y luego en un bucle infinito lee desde el pipe línea por línea, imprime el mensaje leído junto con el PID del proceso padre y el tiempo actual, y repite el proceso.
    Se comprueba si el pipe ya existe en el sistema de archivos. Si no existe, se crea utilizando os.mkfifo().
    Se bifurca el proceso utilizando os.fork(). Si el PID devuelto es diferente de cero, significa que es el proceso padre, por lo que llama a la función parent(). Si el PID es cero, significa que es el proceso hijo, por lo que llama a la función child_v2().

En resumen, el proceso hijo escribe en el pipe, y el proceso padre lee desde él. Ambos procesos ejecutan en bucles infinitos, por lo que la comunicación a través del pipe continua hasta que el programa es terminado manualmente.
"""


import os
import time

luca_pipe= "/tmp/luca_pipe"

def child():
    
    pipeout = os.popen(luca_pipe, os.O_WRONLY)
    counter = 0
    
    while True:
        
        os.write(pipeout, b"Number %03d\n" % counter)
        counter = (counter +1) %5
        time.sleep(1)

def child_v2():
    
    pipeout = open(luca_pipe,"w")
    counter = 0
    
    while True:
        
        pipeout.write("Number %03d\n" % counter)
        counter = (counter +1) % 5
        pipeout.flush()
        time.sleep(1)
    

def parent():
    
    pipein = open(luca_pipe,"r")
    
    while True:
        
        line = pipein.readline()[:-1]
        print("Parent %d got '%s' at %s" % (os.getpid(), line, time.time()))
    

if not os.path.exists(luca_pipe):
    os.mkfifo(luca_pipe)
    

pid = os.fork()

if pid != 0:
    parent()
else:
    child_v2()