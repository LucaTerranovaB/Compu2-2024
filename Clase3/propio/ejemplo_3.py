"""
Popen no es bloqueante, por lo que no va esperar a que termine un proceso para comenzar otro.
Procesos, tareas o hilos concurrentes: ocurren al mismo tiempo
Paralelos: procesos, tareas o hilos concurrentes que se ejecutan en dos núcleos distintos
"""

from subprocess import Popen
import time

for i in range(2):
  Popen(["python", "ejemplo_1.py"])


time.sleep(1)
print('FIN DEL PROCESO PADRE')
