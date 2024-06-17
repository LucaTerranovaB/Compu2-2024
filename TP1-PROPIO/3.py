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
