import os
import signal
import socket
import sys
import multiprocessing
from PIL import Image
import numpy as np
from scipy.ndimage import gaussian_filter

#****************************************************************************************************#
# Punto 1: Carga y División de Imágenes
def cargar_y_dividir_imagen(ruta_imagen, num_partes):
    imagen = Image.open(ruta_imagen)
    imagen_array = np.array(imagen)
    altura, ancho, _ = imagen_array.shape
    partes = []
    altura_parte = altura // num_partes
    for i in range(num_partes):
        inicio = i * altura_parte
        fin = altura if i == num_partes - 1 else (i + 1) * altura_parte
        partes.append(imagen_array[inicio:fin, :, :])
    return partes

#****************************************************************************************************#
# Punto 2: Procesamiento Paralelo
def aplicar_filtro(imagen_parte):
    return gaussian_filter(imagen_parte, sigma=1)

def procesar_en_paralelo(partes):
    with multiprocessing.Pool(processes=len(partes)) as pool:
        resultados = pool.map(aplicar_filtro, partes)
    return resultados


#****************************************************************************************************#
# Punto 3: Comunicación y Sincronización
def trabajador(parte, conn):
    resultado = aplicar_filtro(parte)
    conn.send(resultado)
    conn.close()

def procesar_con_comunicacion(partes):
    procesos = []
    padres = []
    for parte in partes:
        padre, hijo = multiprocessing.Pipe()
        p = multiprocessing.Process(target=trabajador, args=(parte, hijo))
        procesos.append(p)
        padres.append(padre)
        p.start()
    resultados = [padre.recv() for padre in padres]
    for p in procesos:
        p.join()
    return resultados


#****************************************************************************************************#
# Punto 4: Manejo de Señales
def manejador_de_senal(sig, frame):
    print('Interrupción recibida, finalizando...')
    sys.exit(0)

signal.signal(signal.SIGINT, manejador_de_senal)



#****************************************************************************************************#
# Punto 5: Uso de Memoria Compartida
def trabajador_con_memoria_compartida(parte, memoria_compartida, inicio, largo):
    resultado = aplicar_filtro(parte)
    memoria_compartida[inicio:inicio + largo] = resultado.flatten()

def procesar_con_memoria_compartida(partes):
    altura_total = sum([parte.shape[0] for parte in partes])
    ancho = partes[0].shape[1]
    canales = partes[0].shape[2]
    memoria_compartida = multiprocessing.Array('d', altura_total * ancho * canales)
    procesos = []
    inicio = 0
    for parte in partes:
        largo = parte.shape[0] * parte.shape[1] * parte.shape[2]
        p = multiprocessing.Process(target=trabajador_con_memoria_compartida, args=(parte, memoria_compartida, inicio, largo))
        procesos.append(p)
        inicio += largo
        p.start()
    for p in procesos:
        p.join()
    imagen_final = np.frombuffer(memoria_compartida.get_obj()).reshape(altura_total, ancho, canales)
    return imagen_final

if __name__ == "__main__":
    ruta_imagen = 'TP1-PROPIO/um_logo.jpg'  # Cambia esto por la ruta de tu imagen
    num_partes = 4  # Número de partes en las que dividir la imagen

    #****************************************************************************************************#
    # Punto 1: Cargar y dividir la imagen
    partes_imagen = cargar_y_dividir_imagen(ruta_imagen, num_partes)
    
    #****************************************************************************************************#
    # Punto 2: Procesar en paralelo
    resultados_parciales = procesar_en_paralelo(partes_imagen)
    
    #****************************************************************************************************#
    # Punto 3: Procesar con comunicación
    resultados_con_comunicacion = procesar_con_comunicacion(partes_imagen)
    
    #****************************************************************************************************#
    # Punto 5: Procesar con memoria compartida
    imagen_procesada_final = procesar_con_memoria_compartida(partes_imagen)
    
    # Guardar la imagen final procesada
    imagen_procesada = Image.fromarray(imagen_procesada_final.astype('uint8'))
    imagen_procesada.save('imagen_procesada.jpg')
    print("Imagen procesada guardada como 'imagen_procesada.jpg'")