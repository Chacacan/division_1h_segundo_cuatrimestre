from data_desafio_stark_01 import lista_personajes
import os

personajes_femeninos_lista = []
personajes_masculinos_lista = []

def crea_lista_personajes_femeninos(lista_heroes: list):
    for heroe in lista_heroes:
        if heroe.get("genero") == "F":
            personajes_femeninos_lista.append({
                "nombre": heroe.get("nombre"),
                "identidad": heroe.get("identidad"),
                "empresa": heroe.get("empresa"),
                "altura": heroe.get("altura"),
                "peso": heroe.get("peso"),
                "genero": heroe.get("genero"),
                "color_ojos": heroe.get("color_ojos"),
                "color_pelo": heroe.get("color_pelo"),
                "fuerza": heroe.get("fuerza"),
                "inteligencia": heroe.get("inteligencia")
            }
            )
crea_lista_personajes_femeninos(lista_personajes)
def crea_lista_personajes_masculinos(lista_heroes: list):
    for heroe in lista_heroes:
        if heroe.get("genero") == "M":
            personajes_masculinos_lista.append({
                "nombre": heroe.get("nombre"),
                "identidad": heroe.get("identidad"),
                "empresa": heroe.get("empresa"),
                "altura": heroe.get("altura"),
                "peso": heroe.get("peso"),
                "genero": heroe.get("genero"),
                "color_ojos": heroe.get("color_ojos"),
                "color_pelo": heroe.get("color_pelo"),
                "fuerza": heroe.get("fuerza"),
                "inteligencia": heroe.get("inteligencia")
            }
            )
crea_lista_personajes_masculinos(lista_personajes)

# A Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M

def personajes_femeninos(lista_heroes: list):
    for heroe in lista_heroes:
        if heroe.get("genero") == "M":
            print(heroe.get("nombre"))

# B Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F

def personajes_masculinos(lista_heroes: list):

    for heroe in lista_heroes:
        if heroe.get("genero") == "F":
            print(heroe.get("nombre"))

# C Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
def heroe_masculino_mas_alto(personajes_masculinos_lista):
    heroe_mas_alto = None
    for heroe in personajes_masculinos_lista:
        if heroe_mas_alto == None or float(heroe_mas_alto.get("altura")) <= float(heroe.get("altura")):
            heroe_mas_alto = heroe
    return heroe_mas_alto.get("nombre")


# D Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
def heroe_femenino_mas_alto(personajes_femeninos_lista):
    heroe_mas_alto = None
    for heroe in personajes_femeninos_lista:
        if heroe_mas_alto == None or float(heroe_mas_alto.get("altura")) <= float(heroe.get("altura")):
            heroe_mas_alto = heroe
    return heroe_mas_alto.get("nombre")

# E Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
def heroe_mas_bajo_masculino(personajes_masculinos_lista) -> str:
    personaje_mas_bajo = None
    for heroe in personajes_masculinos_lista:
        if personaje_mas_bajo == None or float(personaje_mas_bajo.get("altura")) >= float(heroe.get("altura")):
            personaje_mas_bajo = heroe
    return personaje_mas_bajo.get("nombre")

# F Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
def heroe_mas_bajo_femenino(personajes_femeninos_lista) -> str:
    personaje_mas_bajo = None
    for heroe in personajes_femeninos_lista:
        if personaje_mas_bajo == None or float(personaje_mas_bajo.get("altura")) >= float(heroe.get("altura")):
            personaje_mas_bajo = heroe
    return personaje_mas_bajo.get("nombre")
# G Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
def altura_promedio_masculinos(lista_heroes: list):
    alturas = 0
    cantidad_personajes = 0
    for heroe in lista_heroes:
        if heroe.get("genero") == "M":
            alturas += float(heroe.get("altura"))
            cantidad_personajes += 1
    promedio = round(alturas / cantidad_personajes, 2)
    return promedio
# H Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
def altura_promedio_femeninos(lista_heroes: list):
    alturas = 0
    cantidad_personajes = 0
    for heroe in lista_heroes:
        if heroe.get("genero") == "F":
            alturas += float(heroe.get("altura"))
            cantidad_personajes += 1
    promedio = round(alturas / cantidad_personajes, 2)
    return promedio
# I Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
def informe_de_items_C_F(heroe_masculino_mas_alto,heroe_f_mas_bajo):
    #toma dos parametros devuelto en cada funcion que llama y retorna un strig con sus valores correspondientes
    mensaje = "El heroe mas masculino mas alto es: {0}\nY el heroe femenino mas bajo es: {1}".format(heroe_masculino_mas_alto,heroe_f_mas_bajo)
    return mensaje

# J Determinar cuántos superhéroes tienen cada tipo de color de ojos.

def cantidad_heroes_por_color_ojos(lista_heroes: list):
    #genera una lista con los tipos de color y los nombres de los heroes 
    lista_heroes_por_color_ojos = []
    diccionario_por_color_ojos = {}
    for heroe in lista_heroes:
        color = heroe.get("color_ojos", "sin color")
        nombre = heroe.get("nombre")
        if color not in diccionario_por_color_ojos.keys():
            diccionario_por_color_ojos[color] = [nombre]
        else:
            diccionario_por_color_ojos[color].append(nombre)
    return diccionario_por_color_ojos

def contador_de_personajes_por_color_ojos(diccionario: dict):
    for clave, value in diccionario.items():
        print("\nColor de ojos: {0}\nCantidad de heroes: {1}".format(clave,len(diccionario[clave])))
        
# K Determinar cuántos superhéroes tienen cada tipo de color de pelo.
def cantidad_heroes_por_color_pelo(lista_heroes: list):
    #crea diccionario con los distintos colores de pelo y sus personajes
    lista_heroes_por_color_pelo = []
    diccionario_por_color_pelo = {}
    for heroe in lista_heroes:
        color = heroe.get("color_pelo", "Sin color")
        nombre = heroe.get("nombre")
        if color not in diccionario_por_color_pelo.keys():
            diccionario_por_color_pelo[color] = [nombre]
        else:
            diccionario_por_color_pelo[color].append(nombre)
    return diccionario_por_color_pelo

def contador_de_personajes_por_color_pelo(diccionario: dict):
    for clave, value in diccionario.items():
        print("\nColor de pelo: {0}\nCantidad de heroes: {1}".format(clave,len(diccionario[clave])))

# L Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
def cantidad_heroes_por_tipo_de_inteligencia(lista_heroes: list):
    #
    lista_heroes_por_inteligencia = []
    diccionario_de_inteligencia = {}
    for heroe in lista_heroes:
        inteligencia = heroe.get("inteligencia", "Sin inteligencia")
        nombre = heroe.get("nombre")
        
        if inteligencia not in diccionario_de_inteligencia.keys():
            if heroe.get("inteligencia") == "":
                diccionario_de_inteligencia["No Tiene"] = [nombre]
            else:
                diccionario_de_inteligencia[inteligencia] = [nombre]
        else:
            diccionario_de_inteligencia[inteligencia].append(nombre)
    return diccionario_de_inteligencia

def contador_de_personajes_por_inteligencia(diccionario: dict):
    for clave, value in diccionario.items():
        print("\nTipo de inteligencia: {0}\nCantidad de heroes: {1}".format(clave,len(diccionario[clave])))

# M Listar todos los superhéroes agrupados por color de ojos.
def recorrer_diccionario_para_imprimir_color_ojos(diccionario: dict):
    for clave, value in diccionario.items():
        print("\ncolor de ojos: {0}\nPersonajes: \n".format(clave))
        for personaje in value:
            print("{0}".format(personaje))

# N Listar todos los superhéroes agrupados por color de pelo.
def recorrer_diccionario_para_imprimir_color_pelo(diccionario: dict):
    for clave, value in diccionario.items():
        print("\ncolor de pelo: {0}\nPersonajes: \n".format(clave))
        for personaje in value:
            print("{0}".format(personaje))

# O Listar todos los superhéroes agrupados por tipo de inteligencia
def recorrer_diccionario_para_imprimir_lista_inteligencia(diccionario: dict):
    for clave, value in diccionario.items():
        print("\nTipo de inteligencia: {0}\nPersonajes: \n".format(clave))
        for personaje in value:
            print("{0}".format(personaje))



def mostrar_menu() -> str:
    menu =\
    """
    1 - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
    2 - Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
    3 - Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
    4 - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
    5 - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
    6 - Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
    7 - Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
    8 - Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
    9 - Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    10 - Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    11 - Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
    12 - Listar todos los superhéroes agrupados por color de ojos.
    13 - Listar todos los superhéroes agrupados por color de pelo.
    14 - Listar todos los superhéroes agrupados por tipo de inteligencia
    15 - Salir
    """
    print(menu)
    opcion_elegida = input("Elija una opcion ")
    return opcion_elegida

def limpiar_consola():
    _= input("\npresione una tecla para continuar... ")
    if os.name in ['ce','nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')