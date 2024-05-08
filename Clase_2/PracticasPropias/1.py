import os
 
def main( ):
    print(f"Proceso padre PID: {os.getpid( )}")
    pid = os. fork()

    if pid == 0:
    # Código ejecutado por el proceso hijo
        print(f"Este es el proceso hijo, PID: {os.getpid()}")
    elif pid > 0:
    # Código ejecutado por el proceso
        print(f"Este es el proceso padre, PID todavia: {os.getpid()}")
        os.wait() # El padre espera a que el hijo termine
    else:
    # fork falló
        print("fork falló")

if __name__ == "__main__":
    main()