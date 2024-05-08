#matar procesos

import os
import signal

def bomba_fork():
    while True:
        try:
            # Crear un nuevo proceso hijo
            pid = os.fork()
        except OSError:
            # En caso de error al crear el proceso hijo, salir del bucle
            break
        
        if pid == 0:
            # Código ejecutado por el proceso hijo
            continue
        else:
            # Código ejecutado por el proceso padre
            print("Proceso hijo creado con PID:", pid)

            # Enviar señal SIGKILL para terminar el proceso hijo
            os.kill(pid, signal.SIGKILL)
            print("Proceso hijo con PID", pid, "terminado")

# Llamar a la función de la bomba fork
bomba_fork()
