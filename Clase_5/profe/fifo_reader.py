import os

fifo_path = '/tmp/my_fifo'

print("Opening FIFO...")
with open(fifo_path, 'r') as fifo:
    print("FIFO opened for reading.")
    while True:
        message = fifo.readline().strip()
        if message == "":
            print("No more messages. Exiting.")
            break
        print(f'Received: {message}')
        
        
        
        
#Este código en Python abre un FIFO (First-In-First-Out) para lectura y espera a que lleguen mensajes a través de él. 
#Un FIFO es un mecanismo de comunicación entre procesos que permite que los datos se escriban en un extremo de la tubería y 
#se lean desde el otro extremo en el mismo orden en que se escribieron.
#
#El código intenta abrir el FIFO ubicado en /tmp/my_fifo para lectura utilizando un bloque with para garantizar que el FIFO se cierre correctamente después
#de su uso.
#
#Dentro del bloque with, el código entra en un bucle infinito (while True) donde lee líneas del FIFO usando el método readline()
#y las almacena en la variable message. Luego, comprueba si la línea leída está vacía, lo que indica que no hay más mensajes en el FIFO. 
#En ese caso, imprime un mensaje indicando que no hay más mensajes y sale del bucle. Si la línea no está vacía, imprime el mensaje recibido.
#
#En resumen, este código espera a que lleguen mensajes al FIFO y los imprime a medida que los recibe, y se detiene cuando no hay más mensajes en el FIFO.
