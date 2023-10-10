from data_stark import lista_personajes
import os 
import re

def stark_normalizar_datos(lista_heroes: list) -> None:
    if not lista_heroes:
        print("Error: Lista de heroes vacia")
        return
    for heroes in lista_heroes:    
        for clave, valor in heroes.items():
            if clave in ["altura", "peso", "fuerza"]:
                try:
                    heroes[clave] = float(valor)
                except ValueError:
                    pass
    print("Datos normalizados")
#stark_normalizar_datos(lista_personajes)

def imprimir_dato(un_string: str) -> None:
    #imprime el dato que recibe 
    print(un_string)

def obtener_nombre(heroe: dict)-> str:
    #imprime el nombre del heroe seleccionado
    #devuelve un print por consola
    nombre = "Nombre: {0}".format(heroe["nombre"])
    return nombre

# 1 Crear la función "imprimir_menu_2" que deberá imprimir el menú de opciones por pantalla (las opciones son las mismas del desafío 01). La función no retorna nada. Reutilizar la función 'imprimir_dato' 
def imprimir_menu_2():
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
    imprimir_dato(menu)
#imprimir_menu()

# 2 Crear la función ‘stark_menu_principal_2’ la cual se encargará de imprimir el menú de opciones y le pedirá al usuario que ingrese el número de una de las opciones elegidas y deberá validarlo. En caso de ser correcto dicho número, lo retornara casteado a entero, caso contrario retorna -1. Reutilizar la función 'imprimir_menu_2'
def stark_menu_principal_2():
    imprimir_menu_2()
    seleccion_numero = input("Ingrese la opcion requerida: ") 
    if validar_entero(seleccion_numero):
        seleccion_numero = int(seleccion_numero)
    else:
        seleccion_numero = -1
    return seleccion_numero

# 3 Crear la función 'stark_marvel_app_2' la cual recibirá por parámetro la lista de héroes y se encargará de la ejecución principal de nuestro programa. Utilizar if/elif o match según prefiera (match solo para los que cuentan con python 3.10+). Debe informar por consola en caso de seleccionar una opción incorrecta y volver a pedir el dato al usuario. Reutilizar las funciones con prefijo 'stark_' donde crea correspondiente.

def stark_marvel_app_2(lista_heroes):
    while True:
        opcion_elegida = stark_menu_principal()
        if opcion_elegida == 1:
            pass
        elif opcion_elegida == 2:
            pass
        elif opcion_elegida == 3:
            pass
        elif opcion_elegida == 4:
            pass
        elif opcion_elegida == 5:
            pass
        elif opcion_elegida == 6:
            pass
        elif opcion_elegida == 7:
            pass
        elif opcion_elegida == 8:
            pass
            break
        else:
            imprimir_dato("opcion incorrecta, elija entre 1 y 15")
            
        limpiar_consola()

# 4 Crear la función 'es género' la cual recibirá como parámetros:
# Un diccionario que representará un héroe
# Un string el cual será usado para evaluar si el héroe coincide con el género buscado (el string puede ser ‘M’,  ‘F’ o ‘NB’ ).
# La función deberá retornar True en caso de que cumpla, False caso contrario.
def es_genero(heroe: dict, key: str) -> bool:
    if heroe["genero"] == key:
        return True
    else:
        return False

# 5 Crear la función 'stark_imprimir_heroe_genero' la cual recibirá como parámetros:
# La lista de héroes
# Un string el cual representará el género a evaluar (el string puede ser ‘M’,  ‘F’ o ‘NB’ ). Deberá imprimir solamente los héroes  que coincidan con el género pasado por parámetro.
# Se deberá reutilizar las funciones 'es_genero', 'obtener_nombre' e 'imprimir_dato'.
# La función no retorna nada.
def stark_imprimir_heroe_genero(lista_heroes: list, key: str):
    for heroe in lista_heroes:
        if es_genero(heroe,key):
            imprimir_dato(obtener_nombre(heroe))

# 6 Crear la función 'calcular_min_genero' la cual recibirá como parámetros:
# La lista de héroes. 
# Un string para representar el dato que deberá ser evaluado a efectos de determinar cuál es el máximo de la lista (por ejemplo: “altura”, “peso”, etc)
# Un string para representar el género (el string puede ser ‘M’,  ‘F’ o ‘NB’ )
# La función deberá retornar el héroe que cumpla la condición de tener el mínimo del género especificado
def calcular_min_genero(lista_heroes: list, key: str, genero: str) -> dict:
    heroe_minimo = None
    minimo = None
    for heroe in lista_heroes:
        if heroe["genero"] == "M":
            if minimo == None or minimo >= float(heroe[key]):
                minimo = float(heroe[key])
                heroe_minimo = heroe
        if heroe["genero"] == "F":
            if minimo == None or float(minimo) >= float(heroe[key]):
                minimo = heroe[key]
                heroe_minimo = heroe
        if heroe["genero"] == "NB":
            if minimo == None or float(minimo) >= float(heroe[key]):
                minimo = float(heroe[key])
                heroe_minimo = heroe
    return heroe_minimo
print (calcular_min_genero(lista_personajes,"fuerza","F"))




def limpiar_consola():
    _= input("\npresione una tecla para continuar... ")
    if os.name in ['ce','nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')

def validar_entero(key: str) -> bool:
    return key.isnumeric()
