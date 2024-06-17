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
