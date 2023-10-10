import re
# 1 Escribir una función que reciba un string y devuelva el mismo string todo en mayúsculas.
def todo_mayuscula(texto: str):
    mayuscula = texto.upper()
    return mayuscula

# 2 Escribir una función que reciba un string y devuelva el mismo string todo en minúsculas.
def todo_minuscula(texto: str):
    minuscula = texto.lower()
    return minuscula

# 3 Escribir una función que tome dos strings y devuelva un nuevo string que contenga ambos strings concatenados, separados por un espacio.
def concatenar_dos_strings(texto_1: str , texto_2: str):
    concatenado = texto_1 + " " + texto_2
    return concatenado

# 4 Escribir una función que tome un string y devuelva el número de caracteres que tiene el string.
def longitud_string(texto: str):
    longitud = len(texto)
    return longitud

# 5 Escribir una función que tome un string y un carácter y devuelva el número de veces que aparece ese carácter en el string.
def buscar_caracter(texto: str, caracter: str):
    cantidad = texto.count(caracter)
    return cantidad

# 6 Escribir una función que tome un string y un carácter y devuelva una lista con todas las palabras en el string que contienen ese carácter.
def buscar_palabas_por_caracter(texto: str, caracter: str):
    lista = texto.split()
    
    lista_corregida = []

    for palabras in lista:
        if caracter in palabras:
            lista_corregida.append(palabras)
    return lista_corregida

# 7 Escribir una función que tome un string y devuelva el mismo string con los espacios eliminados
def elimina_espacios(texto: str):
    texto_nuevo = texto.replace(" ","")
    return texto_nuevo

# 8 Escribir una función que reciba dos string (nombre y apellido) y devuelva un diccionario con el nombre y apellido, eliminando los espacios del comienzo y el final y colocando la primer letra en mayúscula
def nombre_y_apellido_corregidos(nombre: str, apellido: str):
    nombre_corregido = nombre.strip().capitalize()
    apellido_corregido = apellido.strip().capitalize()
    diccionario = {"nombre" : nombre_corregido, "apellido" : apellido_corregido}
    return diccionario

# 9 Escribir una función que tome una lista de nombres y los una en una sola cadena separada por un salto de línea, por ejemplo: ["Juan", "María", "Pedro"] -> "Juan\nMaría\nPedro".
def agrega_salto_de_linea_en_strings(lista: list) -> str:
    lista_corregida = "\n".join(lista)
    return lista_corregida

# 10 Escribir una función que tome un nombre y un apellido y devuelva un email en formato "inicial_nombre.apellido@utn-fra.com.ar".
def formato_mail(nombre: str, apellido: str):
    mail = "{}.{}@utn-fra.com.ar".format(nombre[0].lower(), apellido.lower())
    return mail

# 11 Escribir una función que tome una lista de palabras y devuelva un string que contenga todas las palabras concatenadas con comas y "y" antes de la última palabra. Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"], el string resultante debería ser "manzanas, naranjas y bananas"..
def concatenar_palabras(lista: list) -> str:
    texto_nuevo = " y ".join(lista)
    texto_nuevo = texto_nuevo.replace(" y ", ", ",(texto_nuevo.count(" y ")-1))
    return texto_nuevo
#print(concatenar_palabras(["manzanas", "naranjas", "bananas","toronja"]))

# 12 Escribir una función que tome un número de tarjeta de crédito como input, verificar que todos los caracteres sean numéricos y devolver los últimos cuatro dígitos y los primeros dígitos como asteriscos, por ejemplo: "**** **** **** 1234". 
def verificacion_tarjeta():
    while True:
        numero_de_tarjeta = input("Ingrese los 16(doce) digitos de su tarjeta: ")
        if numero_de_tarjeta.isnumeric() and len(numero_de_tarjeta) == 16:
            return "**** **** **** {0}".format(numero_de_tarjeta[-4:])
            break
        else:
            print("numero de tarjeta invalido, vuelva a intentarlo")

# 13 Escribir una función que tome un correo electrónico y elimine cualquier carácter después del símbolo @, por ejemplo: "usuario@gmail.com" -> "usuario".
def elimina_posterior_asterisco(texto: str):
    texto_lista = texto.split("@")
    texto_limpio = texto_lista[0]
    return texto_limpio

# 14 Escribir una función que tome una URL y devuelva solo el nombre de dominio, por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..
def devuelve_dominio(texto: str):
    texto_nuevo = texto.split(".")
    texto_2 = texto_nuevo[1]
    return texto_2

# 15 Escribir una función que tome una cadena de texto y devuelva solo los caracteres alfabéticos, eliminando cualquier número o símbolo (sólo son válidos letras y espacios), por ejemplo: "H0l4, m4nd0!" -> "Hl mnd”
def filtra_alfabeto(texto: str):
    #re. findall(): Busca todas las ocurrencias de un patrón en una cadena y devuelve una lista de cadenas que coinciden.
    texto_filtrado = re.findall(r"[a-zA-Z ' ']+",texto)
    texto_filtrado = "".join(texto_filtrado)
    return texto_filtrado

# 16 Escribir una función que tome una cadena de texto y la convierta en un acrónimo, tomando la primera letra de cada palabra, por ejemplo: "Universidad Tecnológica Nacional Facultad Regional Avellaneda" -> "UTNFRA”.
def convierte_texto_en_acronimo(texto: str):
    lista_de_palabras = texto.split()

    texto_para_iniciales = ""

    for palabra in lista_de_palabras:
        texto_para_iniciales += palabra[0].upper()
    return texto_para_iniciales
# print(convierte_texto_en_acronimo("Universidad Tecnológica Nacional Facultad Regional Avellaneda"))

# 17 Escribir una función que tome un número binario y lo convierta en una cadena de 8 bits, rellenando con ceros a la izquierda si es necesario, por ejemplo: "101" -> "00000101".
def rellena_hasta_ocho_digitos_con_cero(numero: int) -> str:
    ocho_bits = str(numero).zfill(8)
    return ocho_bits
#print(rellena_hasta_ocho_digitos_con_cero(101))

# 18 Escribir una función que tome una cadena de caracteres y reemplace todas las letras mayúsculas por letras minúsculas y todas las letras minúsculas por letras mayúsculas, por ejemplo: "HoLa" -> "hOlA"
def cambia_mayusculas_y_minusculas(texto: str) -> str:
    texto_nuevo = ""
    for letra in texto:
        if letra.islower():
            texto_nuevo+= letra.upper()
        elif letra.isupper():
            texto_nuevo+= letra.lower()
        else:
            texto_nuevo+= letra
    return texto_nuevo

# 19 Escribir una función que tome una cadena de caracteres y cuente la cantidad de dígitos que contiene, por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.
def cuenta_cantidad_de_numeros(texto: str) -> int:
    contador = 0
    for letra in texto:
        if letra.isnumeric():
            contador+= 1
    return contador

# 20 Escribir una función que tome una lista de direcciones de correo electrónico y las una en una sola cadena separada por punto y coma, por ejemplo: ["juan@gmail.com", "maria@hotmail.com"] -> "juan@gmail.com;maria@hotmail.com".
def concatena_mails(lista) -> str:
    texto = ";".join(lista)
    return texto
print(concatena_mails(["juan@gmail.com", "maria@hotmail.com"]))
# 21 Crear una función que reciba como parámetro un string y devuelva un diccionario donde cada clave es una palabra y cada valor es un entero que indica cuántas veces aparece esa palabra dentro del string.
def cuenta_palabras(texto: str) -> dict:
    diccionario = {}
    lista_vacia = texto.split()
    for palabra in lista_vacia:
        if not palabra in diccionario:
            diccionario[palabra] = 1
        else:
            diccionario[palabra] += 1
    return diccionario
print(cuenta_palabras("pablito clavo un clavito que clavito clavo pablito"))