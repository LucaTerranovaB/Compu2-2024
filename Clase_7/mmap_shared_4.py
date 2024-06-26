import mmap
import os
import signal
import time

def lee(s, f):
    leido = area.read(16)
    area.seek(0)
    area.write(leido.decode().upper().encode())
    os.kill(pid, signal.SIGUSR1)

def lee_upper(s, f):
    print(area.read(16))


signal.signal(signal.SIGUSR1, lee)

area = mmap.mmap(-1, 16)

pid = os.fork()

if pid == 0:    
    signal.signal(signal.SIGUSR1, lee_upper)
    area.write(b'soy el hijo')
    os.kill(os.getppid(), signal.SIGUSR1)
    area.seek(0)
    # time.sleep(2)
    signal.pause()
    exit()

time.sleep(1)
os.wait()
