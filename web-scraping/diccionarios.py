diccionario = {}

print(diccionario)
print(type(diccionario))

#asignacion de valorea al diccionario
diccionario["nombre"] = "Gregory"
diccionario["edad"] = 20

print(diccionario)

#obtener valor vinculado a una llave
print(diccionario["nombre"])
print(diccionario["edad"])


diccionario2 = {
    "nombre": "alberto",
    "edad": 20,
    5.1: 10,
    "vocales": ["a", "e", "i", "o", "u"],
    (7,2): 50
}

print(len(diccionario2))
print(diccionario2[(7,2)])
del(diccionario2["edad"])
print(diccionario2)