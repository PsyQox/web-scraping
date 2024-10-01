from random import *

x = 0

for i in range(10):
    x += randint(1,10)
    if i == 9:
        print("Se termino la iteracion")
    else:
        print(x, "Este numero le corresponde a la iteracion numero: ", i)


print("su total de la suma: ", x)
