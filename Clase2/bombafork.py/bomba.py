import os
import resource
import time 
import sys

class BombaFork():
    
    max_procesos = 100
    
    def obtener_limites_recursos(max_procesos):
        soft,hard = resource.getrlimit(resource.RLIMIT_NPROC)
        print("Límite suave:", soft)
        time.sleep(5)
        print("Límite duro:", hard)
        time.sleep(5)
        print("---------------------------------- \n")
    
        #establecemos un nuevo límite más bajo
        resource.setrlimit(resource.RLIMIT_NPROC, (max_procesos, hard))
        print("Límite de procesos hijo establecido en", max_procesos)
        time.sleep(5)
        
    def bomba_fork(max_procesos):
        max_procesos = 100
        
        while max_procesos <= 100:
            
            for i in range(max_procesos):
                # Crear un nuevo proceso hijo
                pid = os.fork()
                time.sleep(2)
            
            
            if pid == 0:
                # Código ejecutado por el proceso hijo
                time.sleep(2)
                continue
            else:
                time.sleep(2)
                print("Proceso hijo creado con PID:", pid)
                print("---------------------------------- \n")
                
if __name__ == "__main__":
    # Llamar a la función para establecer el límite de procesos
    BombaFork.obtener_limites_recursos(100)
    # Ejecutar la bromba fork
    BombaFork.bomba_fork()    
    
            