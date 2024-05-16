import os

r,w = os.pipe()

r = os.fdopen(r)
w = os.fdopen(w,'w')

mensaje= input("Ingrese un mensaje")

w.write(mensaje)
w.close()

print("Mensaje Leido: ", r.readline)

r.close()




# Este código en Python crea un pipe (tubería) utilizando la función os.pipe(), 
# que devuelve un par de descriptores de archivos que representan los extremos de lectura y escritura de la tubería.
#
# Luego, el código intenta abrir los descriptores de archivos para lectura (r) y escritura (w). 
# Sin embargo, hay un error en esta parte del código.
#  La función os.fdopen() espera un descriptor de archivo, pero en lugar de pasar el descriptor, 
#  se está asignando un objeto de archivo devuelto por os.fdopen() a las variables r y w. 
# Esto sobrescribe los descriptores de archivos con los objetos de archivo y los descriptores de archivos originales se pierden. 
# Esto ocasionará un error más adelante cuando se intenten cerrar los descriptores de archivo.
#
# Después, el código solicita al usuario que ingrese un mensaje y escribe este mensaje en el extremo de escritura de la tubería (w) utilizando el método write().
#
#
# El extremo de escritura de la tubería se cierra con w.close().
#
# Luego, intenta leer el mensaje del extremo de lectura de la tubería (r) utilizando el método readline().
# Sin embargo, hay un error aquí también. El método readline() necesita ser llamado como una función r.readline(), 
#
# pero el código lo está llamando sin los paréntesis, lo que simplemente hace referencia a la función en sí y no la ejecuta.
# Esto significa que el mensaje no se lee correctamente.
#
# Finalmente, el código intenta cerrar el extremo de lectura de la tubería (r), 
# pero debido a que r ha sido sobrescrito con un objeto de archivo devuelto por os.fdopen(), esto también causará un error.
# 
# En resumen, el código intenta crear una tubería, escribir un mensaje en ella, leer el mensaje y cerrar la tubería, 
# pero debido a los errores mencionados, no logra hacerlo correctamente.