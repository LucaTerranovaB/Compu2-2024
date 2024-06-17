import signal
import sys

def manejador_de_senal(sig, frame):
    print('Interrupción recibida, finalizando...')
    sys.exit(0)

# Configurar el manejador de señales
signal.signal(signal.SIGINT, manejador_de_senal)

# Ahora, al presionar Ctrl+C, se imprimirá el mensaje y se cerrará el programa limpiamente.
