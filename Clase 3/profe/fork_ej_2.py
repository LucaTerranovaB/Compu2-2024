"""
Se pueden ver los procesos con ps lf.
Para ver los procesos padre se pueden ver con ps ps
"""


import os
import sys
import time

print('SOY EL PADRE (PID: %d)' % os.getpid())
print('--------------------------------')
try:
  ret = os.fork()
except OSError:
  print('ERROR AL CREAR EL HIJO')
  

while True:
  if ret > 0:
    print('SOY EL PADRE (PID: %d )' % os.getpid())
#    break#Con este break se deja huerfano al hijo
#    sys.exit(0)
    
  elif ret == 0:
    print('SOY EL HIJO (PID: %d -- PPID: %d)' % (os.getpid(), os.getppid()))
#    break #Con este break se genera un hijo zombie
#    sys.exit()
  
  time.sleep(1)
  print()
  


