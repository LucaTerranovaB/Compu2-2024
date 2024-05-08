"""
    Este código en Python define una función funcionUSR2 que maneja la señal SIGUSR2 (una señal personalizada) cuando se recibe. 
    La función simplemente imprime un mensaje indicando que se ha recibido la señal y muestra información sobre el marco del proceso.

La función main configura la señal SIGUSR1 para que sea ignorada (signal.SIG_IGN) y configura la señal SIGUSR2 para que llame a funcionUSR2 cuando se reciba. 
Luego, imprime información sobre varias señales predefinidas y sus manejadores de señales actuales.

El programa luego entra en un estado de espera (sleep(1000)) durante 1000 segundos (aproximadamente 16 minutos), 
durante los cuales está esperando recibir señales. 
Cuando se recibe una señal SIGUSR2, la función funcionUSR2 se ejecutará y mostrará el mensaje correspondiente. 
Después de eso, el programa imprimirá "Saliendo" y finalizará.

Es importante tener en cuenta que el código intenta imprimir el manejador de señales para la señal SIGKILL,
pero esto no es posible ya que SIGKILL y SIGSTOP son señales que no pueden ser manejadas o ignoradas en Python. 
Esto es porque SIGKILL y SIGSTOP son señales que fuerzan la terminación o la suspensión de un proceso y no pueden ser manipuladas por el programa.
"""

from time import sleep
import signal,os


def funcionUSR2(s, frame):
    
    print("Recibiendo señal USR ", s)
    print("Frame: ", frame)
    
    

def main():
    
    print("kill -USR2 ", os.getpid)
    
    
    #-9 -2 -USR1/2 -STOP
    #sig stop y sig kill no pueden modificarse!!
    
    print("Señal 2: "    + str(signal.getsignal(signal.SIGINT)))
    print("Señal USR1: " + str(signal.getsignal(signal.SIGUSR1)))
    print("Señal USR2: " + str(signal.getsignal(signal.SIGUSR2)))
    print("Señal STOP: " + str(signal.getsignal(signal.SIGSTOP)))
    print("Señal KILL: " + str(signal.getsignal(signal.SIGKILL))) 
    
    sleep(10)
    
    
    
    print("Saliendo")


if __name__ == '__main__':
    main()
    