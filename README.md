# Trabajo Práctico Nº 1: Procesamiento de Imágenes en Paralelo

## Introducción
Este trabajo práctico consiste en desarrollar una aplicación que procese imágenes utilizando técnicas de procesamiento paralelo en Python. Los conceptos clave que se abordarán incluyen el manejo de procesos y subprocesos, la comunicación entre procesos, el manejo de señales y el uso de memoria compartida.

El objetivo principal es dividir una imagen en partes iguales, aplicar un filtro matemático simple a cada parte en paralelo, y luego combinar los resultados en una imagen final. Los alumnos deberán agregar funcionalidades en cada punto.

### Punto 1: Carga y División de Imágenes

**Objetivo:**
Desarrollar una función que cargue una imagen y la divida en partes iguales para ser procesadas en paralelo.

**Instrucciones:**
1. **Carga de Imagen:** Utilizar una biblioteca como `PIL` (Pillow) o `OpenCV` para cargar la imagen desde el disco.
   - Documentación de PIL: https://pillow.readthedocs.io/en/stable/
   - Documentación de OpenCV: https://docs.opencv.org/master/d6/d00/tutorial_py_root.html
2. **División de Imagen:** Dividir la imagen en `n` partes iguales (donde `n` es el número de procesos a crear). Cada parte debe ser un segmento continuo de la imagen original.
3. **Almacenamiento de Partes:** Guardar cada parte de la imagen en una lista o array para ser procesada posteriormente.

### Punto 2: Procesamiento Paralelo

**Objetivo:**
Implementar el procesamiento paralelo de las partes de la imagen utilizando procesos y aplicar un filtro matemático simple.

**Instrucciones:**
1. **Definición de Filtro:** Crear una función que aplique un filtro (por ejemplo, un filtro de desenfoque) a una parte de la imagen.
   - Documentación de `scipy.ndimage`: https://docs.scipy.org/doc/scipy/reference/ndimage.html
2. **Creación de Procesos:** Utilizar el módulo `multiprocessing` para crear un proceso por cada parte de la imagen.
   - Documentación de `multiprocessing`: https://docs.python.org/3/library/multiprocessing.html
3. **Aplicación del Filtro:** Cada proceso debe aplicar el filtro a su respectiva parte de la imagen y devolver el resultado.

### Punto 3: Comunicación y Sincronización

**Objetivo:**
Implementar la comunicación entre procesos utilizando Pipes y FIFO para coordinar el procesamiento.

**Instrucciones:**
1. **Comunicación con Pipes:** Utilizar `multiprocessing.Pipe` para comunicar resultados parciales entre procesos.
   - Documentación de `multiprocessing.Pipe`: https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Pipe
2. **Proceso Coordinador:** Crear un proceso coordinador que reciba los resultados parciales de los procesos trabajadores y los combine.
3. **Sincronización:** Asegurar que todos los procesos finalicen su ejecución antes de combinar los resultados.

### Punto 4: Manejo de Señales

**Objetivo:**
Implementar el manejo de señales para permitir la interrupción controlada del procesamiento.

**Instrucciones:**
1. **Configuración de Señales:** Configurar una señal (por ejemplo, `SIGINT`) para interrumpir los procesos de forma controlada.
   - Documentación de `signal`: https://docs.python.org/3/library/signal.html
2. **Manejador de Señales:** Implementar un manejador de señales en el proceso principal para capturar la interrupción y realizar una limpieza adecuada.
3. **Interrupción Controlada:** Asegurarse de que los procesos trabajadores puedan ser interrumpidos y que liberen recursos de manera segura.

### Punto 5: Uso de Memoria Compartida

**Objetivo:**
Utilizar memoria compartida para almacenar resultados parciales y combinarlos en el proceso principal.

**Instrucciones:**
1. **Creación de Memoria Compartida:** Utilizar `multiprocessing.Array` para crear un array compartido entre procesos.
   - Documentación de `multiprocessing.Array`: https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Array
2. **Almacenamiento de Resultados:** Modificar los procesos trabajadores para almacenar los resultados parciales en la memoria compartida.
3. **Combinación de Resultados:** Leer los resultados almacenados en la memoria compartida y combinarlos en una imagen final.
