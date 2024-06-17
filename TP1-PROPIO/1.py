from PIL import Image
import numpy as np

def cargar_y_dividir_imagen(ruta_imagen, num_partes):
    # Cargar la imagen
    imagen = Image.open(ruta_imagen)
    imagen_array = np.array(imagen)
    
    # Obtener dimensiones de la imagen
    altura, ancho, _ = imagen_array.shape
    partes = []
    
    # Dividir la imagen en partes iguales verticalmente
    altura_parte = altura // num_partes
    for i in range(num_partes):
        inicio = i * altura_parte
        if i == num_partes - 1:
            # Asegurarse de incluir cualquier resto en la última parte
            fin = altura
        else:
            fin = (i + 1) * altura_parte
        partes.append(imagen_array[inicio:fin, :, :])
    
    return partes

# Ejemplo de uso
ruta_imagen = 'TP1-PROPIO/um_logo.jpg'  # Cambia esto por la ruta de tu imagen
num_partes = 4  # Número de partes en las que dividir la imagen
partes_imagen = cargar_y_dividir_imagen(ruta_imagen, num_partes)

# Verificar la cantidad de partes obtenidas
print(f'Imagen dividida en {len(partes_imagen)} partes')


import multiprocessing
from scipy.ndimage import gaussian_filter


def aplicar_filtro(imagen_parte):
    # Aplicar un filtro de desenfoque gaussiano
    return gaussian_filter(imagen_parte, sigma=1)

def procesar_en_paralelo(partes):
    with multiprocessing.Pool(processes=len(partes)) as pool:
        resultados = pool.map(aplicar_filtro, partes)
    return resultados

# Ejemplo de uso
resultados_parciales = procesar_en_paralelo(partes_imagen)

# Verificar que el procesamiento haya generado el mismo número de partes
print(f'Se procesaron {len(resultados_parciales)} partes')


import multiprocessing

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
    
    resultados = []
    for padre in padres:
        resultados.append(padre.recv())
    
    for p in procesos:
        p.join()
    
    return resultados

# Ejemplo de uso
resultados_con_comunicacion = procesar_con_comunicacion(partes_imagen)

# Verificar la cantidad de resultados
print(f'Se obtuvieron {len(resultados_con_comunicacion)} resultados a través de pipes')
