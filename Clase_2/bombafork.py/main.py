import os
import resource

def limitar_procesos():
    # Establecer el límite de procesos hijo
    max_procesos = 100  # Puedes ajustar este número según tus necesidades
    
    # Obtener los límites actuales del sistema
    soft, hard = resource.getrlimit(resource.RLIMIT_NPROC)
    
    # Establecer un nuevo límite más bajo
    resource.setrlimit(resource.RLIMIT_NPROC, (max_procesos, hard))
    print("Límite de procesos hijo establecido en", max_procesos)

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


if __name__ == "__main__":
# Llamar a la función para establecer el límite de procesos
    limitar_procesos()

# Llamar a la función de la bomba fork
    bomba_fork()