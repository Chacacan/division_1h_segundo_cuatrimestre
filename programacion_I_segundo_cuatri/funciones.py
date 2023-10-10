""" 1 Crear una función que convierta grados Celsius a grados Fahrenheit. Recibe un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.
"""
# def grados_celcius_a_fahrenheit(temperatura):
#     resultado = temperatura * 1.8 + 32
#     return resultado

# print(grados_celcius_a_fahrenheit(20))

"""2 Crear una función que calcule el área de un círculo. Recibe un parámetro (radio) y devuelve el área del círculo.
"""
# import math
# def area_de_circulo(radio):
#     resultado =  round(math.pi * radio**2, 2)
#     return resultado
# print(area_de_circulo(2))

"""3 Crear una función que calcule el descuento aplicado a un producto. Recibe dos parámetros (precio original y precio con descuento) y devuelve el porcentaje de descuento aplicado.
"""
# def descuento_aplicado(precio_original , precio_descuento):
#     resultado = precio_descuento * 100 /precio_original
#     return resultado
# print(descuento_aplicado(100 , 80))

"""4 Crear una función que calcule el promedio de edad de un grupo de personas. Recibe una lista de edades y devuelve el promedio.
"""
# nombres_con_edades ={
#     "rogelio" : 24,
#     "roberto" :63,
#     "samira" : 32,
#     "yasuo" : 30
# }
# def promedio_de_edades(lista_nombres: list):
#     edad = 0
#     cantidad_de_personas = 0
#     for nombres in lista_nombres:
#         edad += lista_nombres[nombres]
#         cantidad_de_personas +=1
#     if cantidad_de_personas > 0:
#         promedio_edad = round(edad / cantidad_de_personas, 2)
#     else:promedio_edad
#     return promedio_edad
# print(promedio_de_edades(nombres_con_edades))

"""5 Crear una función que determine si un número es primo o no. Recibe un parámetro (número) y devuelve True si es primo y False si no lo es.
""" 
# def si_es_o_no_primo_un_numero(numero: int):
#     es_primo = True
#     for i in range(2,numero):
#         print(i)
#         if numero % i == 0:
#             es_primo = False
#     return es_primo
# print(si_es_o_no_primo_un_numero(7))

"""6 Crear una función que calcule el área de un triángulo. Recibe dos parámetros (base y altura) y devuelve el área.
"""
# def calculo_area_triangulo(base: float, altura: float):
#     area = round((base * altura) / 2, 2)
#     return area

# print(calculo_area_triangulo(5,10))

"""7 Crear una función que calcule el máximo común divisor de dos números. Recibe dos parámetros (números) y devuelve el máximo común divisor.
"""
def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a


numero1 = 13
numero2 = 5
mcd = calcular_mcd(numero1, numero2)
print(f"El máximo común divisor de {numero1} y {numero2} es {mcd}.")
    
"""8 Crear una función que verifique si un número es par o impar. Recibe un número como parámetro y devuelve True si es par o False si es impar.
"""
# def numero_par_o_impar(numero: int) -> bool:
#     if numero % 2 == 0:
#         return True
#     else:
#         return False
# print(numero_par_o_impar(3))


""" 9 Crear una función que cuente la cantidad de veces que aparece un elemento en una lista. Recibe una lista y un elemento como parámetros y devuelve la cantidad de veces que aparece en la lista.
"""
# lista_random = [
#     1,
#     "rodrigo",
#     "True",
#     True,
#     1,
#     "1"
# ]
# def contador_repetidos_lista(lista, elemento_a_evaluar):
#     contador = lista_random.count(elemento_a_evaluar)
#     return contador

# print(contador_repetidos_lista(lista_random,"True"))



# """10 Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.
# """
# palabras = [
#     "caracol",
#     "unicef",
#     "elefante",
#     "salado"
# ]
# def devuelve_palabra_mas_larga(lista: list) -> str:
#     item_mas_largo = lista[0]
#     for i in range (len(lista)):
#         if len(lista[i]) >= len(lista[0]):
#             item_mas_largo = lista[i]
#     return item_mas_largo

# print(devuelve_palabra_mas_larga(palabras))

# """11 Crea una función que reciba como parámetro una cadena de texto y devuelva la cantidad de vocales que tiene.
# """
# def cuenta_vocales_de_str(palabra: str):
#     letra_a = 0
#     letra_e = 0
#     letra_i = 0
#     letra_o = 0
#     letra_u = 0
#     for i in range (len(palabra)):
#         match (palabra[i].capitalize()):
#             case "A":
#                 letra_a += 1
#             case "E":
#                 letra_e += 1
#             case "I":
#                 letra_i += 1
#             case "O":
#                 letra_o += 1
#             case "U":
#                 letra_u += 1
#     resultado = "La cantidad de vocales son: \n A = {0}\n E = {1}\n I = {2}\n O = {3}\n U = {4}\n ".format(letra_a, letra_e, letra_i, letra_o, letra_u)
#     return resultado

# print(cuenta_vocales_de_str("elefante, comadreja"))


# """12 Crea una función que reciba dos listas de nombres, y devuelva una lista con los nombres que aparecen en ambas listas
# """
# nombres_1 = [
#     "Magic mike",
#     "Roberto",
#     "Jose",
#     "Maria"
# ]

# nombres_2 = [
#     "Lisandro",
#     "Roberto",
#     "Pedro",
#     "Maria"
# ]
# def nombres_iguales(lista_1: list, lista_2: list) -> str:
#     nombre_repetido = []
#     for nombre in lista_1:
#         if nombre in lista_2:
#             nombre_repetido.append(nombre)
#     return nombre_repetido
# print(nombres_iguales(nombres_1,nombres_2))

# """13 Crear una función que recibe una lista de palabras y devuelve un diccionario con las palabras como llaves y su longitud como valores.
# """
# nombres_1 = [
#     "Magic mike",
#     "Roberto",
#     "Jose",
#     "Maria"
# ]
# def crea_diccionario(lista_palabras: str):
#     diccionario_de_palabras = {}
#     for clave in lista_palabras:
#         diccionario_de_palabras[clave] = (len(clave))
#     return diccionario_de_palabras
# print(crea_diccionario(nombres_1))

# """14 Crear una función que recibe una lista de números y devuelve un diccionario con el valor mínimo, el valor máximo y el promedio de los números en la lista.
# """
# lista_de_prueba = [1,2,3,4,5,6,7,8,9,10]

# def valor_min_max_promedio(lista: list):
#     maximo = 0
#     minimo = 0
#     suma_de_numeros = 0
#     if len(lista) >= 0 :
#         minimo = lista[0]
#         maximo = lista[0]
    
#     for i in lista :
#         suma_de_numeros += i
#         if i >= maximo:
#             maximo = i
#         if i <= minimo:
#             minimo = i
#     promedio = suma_de_numeros / len(lista)
#     diccionario_de_respuesta = {
#         "valor maximo" : maximo,
#         "valor minimo" : minimo,
#         "promedio de los numeros" : promedio
#     }
#     return diccionario_de_respuesta
# print(valor_min_max_promedio(lista_de_prueba))

# """15 Crear una función que recibe una lista de diccionarios con información de películas (título, género, director) y devuelve un diccionario con la cantidad de películas por género.
# """

# lista_peliculas = [
#     {"titulo": "la pistola desnuda", "genero": "comedia", "director": "Director1"},
#     {"titulo": "Pelicula2", "genero": "Drama", "director": "Director2"},
#     {"titulo": "la pistola desnuda 2", "genero": "comedia", "director": "Director3"},
# ]

# def cantidad_peliculas_por_genero(lista_peliculas_evaluar):
#     generos = {}
#     for pelicula in lista_peliculas_evaluar:
#         genero = pelicula.get("genero")
#         if genero in generos:
#             generos[genero] += 1
#         else:
#             generos[genero] = 1

#     return generos
# print(cantidad_peliculas_por_genero(lista_peliculas))

def limpiar_consola() -> None:
    """
    Imprime un mensaje indicando que limpiará la consola al presionar la tecla enter.
        Para que funcione hay que importar el modulo os de la siguiente manera:
        import os
    Recibe: Nada
    Devuelve: Nada
    """
    _ = input("\nPresione enter para continuar... ")
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')