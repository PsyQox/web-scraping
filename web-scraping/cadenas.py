cadena = "El perro corre rapido"
cadena_corta = "EL PERRO CORRE RAPIDO"

#multiplicador de cadenas
print(cadena * 2)

#cortar cadenas
print(cadena_corta[0:3])
#muestra el ultimo digito
print(cadena_corta[-1])

#metodos de cadenas
    #len print(len(cadena))
    #print(cadena.find("o")) Busca la posicion del primer caracter
print(cadena.count("o")) #cuenta la cantidad de veces que aparece un caracter   
print(cadena.capitalize()) #pone la primera letra en mayuscula
print(cadena.upper()) #pone todo en mayuscula
print(cadena.lower()) #pone todo en minuscula
print(cadena.replace("perro", "gato")) #reemplaza una palabra por otra si le pongo otro argumento es para la cantidad a remplazar
print(cadena.split(" ")) #separa la cadena en una lista
print(cadena.strip()) #elimina los espacios en blanco al inicio y al final
print(cadena.startswith("El")) #verifica si la cadena comienza con un caracter
print(cadena.endswith("rapido")) #verifica si la cadena termina con un caracter
print(cadena.isnumeric()) #verifica si la cadena es un numero
print(cadena.isalpha()) #verifica si la cadena es alfabetica
print(cadena.isalnum()) #verifica si la cadena es alfanumerica
print(cadena.islower()) #verifica si la cadena esta en minuscula
print(cadena.isupper()) #verifica si la cadena esta en mayuscula
print(cadena.istitle()) #verifica si la cadena esta en titulo
print(cadena.isprintable()) #verifica si la cadena es imprimible
print(cadena.isidentifier()) #verifica si la cadena es un identificador
print(cadena.isascii()) #verifica si la cadena es ascii
print(cadena.isdecimal()) #verifica si la cadena es decimal
print(cadena.isdigit()) #verifica si la cadena es digito
print(cadena.isnumeric()) #verifica si la cadena es numerico
print(cadena.isprintable()) #verifica si la cadena es imprimible
print(cadena.isidentifier()) #verifica si la cadena es un identificador

