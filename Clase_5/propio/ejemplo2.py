"""
    Este código en Python utiliza el módulo os para crear un proceso hijo que escribe en un pipe, y un proceso padre que lee de ese pipe.

Aquí está el flujo del programa:

    Se importa el módulo os.
    Se llama a os.pipe(), que crea un par de descriptores de archivo conectados a un pipe.
    Se llama a os.fork(), lo que crea un nuevo proceso. En el proceso padre, pid contendrá el PID (identificador de proceso) del proceso hijo, mientras que en el proceso hijo pid será 0.
    En el proceso padre (if pid:), se imprime el PID del proceso padre (os.getpid()), se cierra el extremo de escritura del pipe y se abre el extremo de lectura como un objeto de archivo (os.fdopen(r)). Luego, lee desde el pipe y espera a que el proceso hijo termine (os.wait()).
    En el proceso hijo (else:), se imprime el PID del proceso hijo (os.getpid()), se cierra el extremo de lectura del pipe y se abre el extremo de escritura como un objeto de archivo con modo escritura (os.fdopen(w, 'w')). Luego, escribe en el pipe y cierra el extremo de escritura del pipe.
    Ambos procesos esperan a que el usuario presione Enter antes de salir.

En resumen, el proceso hijo escribe en el pipe y el proceso padre lee lo que escribió el hijo desde el pipe. Una vez que se completa la lectura, ambos procesos terminan.

"""

import os
    
r,w = os.pipe()

pid = os.fork()


if pid:
    print("P:" ,os.getpid())
    
    #os.close(w)
    
    r = os.fdopen(r)
    print("P: leyendo")
    
    string = r.readline()
    
    print("P: text = ",string)
    os.wait()
    
    input()
    exit()
    
else:
    print("H: ",os.getpid())
    #os.close(w)
    
    w = os.fdopen(w, 'w')
    print("H: Escribiendo")
    
    w.write("Texto escrito por el hijo\n")
    w.close()
    
    print("H: Hijo cerrado")
    input()
    exit()
    