import os

r,w = os.pipe()

r = os.fdopen(r)
w = os.fdopen(w,'w')

mensaje= input("Ingrese un mensaje")

w.write(mensaje)
w.close()

print("Mensaje Leido: ", r.readline)

r.close()