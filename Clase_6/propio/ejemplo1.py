import os
import signal
import time 


#Funcion que maneja la señal SIGUSR1

def time_handler(sig, frame):

    global timer_running
    timer_running = False
    
    
#Funcion que inicia un temporizador con una duracion especifica en segundos

def start_timmer(seconds):
    
    global timer_running
    timer_running= True
    
    #Establaece el manehjador de señal para SIGUSR1 como la funcion time_handler
    
    signal.signal(signal.SIGUSR1, time_handler)
    print(f"Timer started for {seconds} seg.")
    
    #Ciclo que cuennta hacia atras el tiempo restante hasta que el temporizado llegue a cero o pare
   
    while seconds > 0 and timer_running:
        
        print(f"Remainig time: {seconds},seconds")
        time.sleep(1)
        
        #reduce el contador de tiempo en un segundo
        
        seconds -= 1
        
    #Si el contador llega a cer imprime un mensaje
    if seconds == 0:
        print("Timer finished") 
        

#Funcion del programa

def main():
    
    print("process ID: ",os.getpid) #Proceso acrual
    print("send SIGUSR1 to start de timer") #Indica como iniciar el temporaizador
    
    while True:
        choice = input("Enter 'q' to quit: ")  # Solicita al usuario ingresar una opción
        if choice.lower() == 'q':  # Si el usuario ingresa 'q', termina el bucle
            break
        elif choice.lower() == 'start':  # Si el usuario ingresa 'start', solicita el número de segundos para el temporizador
            seconds = int(input("Enter the number of seconds for the timer: "))
            start_timmer(seconds)  # Inicia el temporizador con la duración especificada

# Entrada principal del programa
if __name__ == "__main__":
    main()  # Llama a la función principal del programa
    
    
    
#Este código define una aplicación de temporizador que cuenta hacia atrás desde un número especificado
#de segundos. El usuario puede iniciar el temporizador ingresando 'start' y especificando la duración 
#del temporizador. 
#El temporizador se detiene cuando se recibe la señal SIGUSR1 o cuando alcanza cero. 
#El usuario puede salir del programa ingresando 'q'.

    