from dicccionario_heroes import lista_personajes
#B Recorrer la lista imprimiendo por consola el nombre de cada superhéroe

def imprimir_nombre_personajes(lista_heroes: list[dict]):
    #recorre la lista de heroes e imprime cada nombre de la lista
    for heroe in lista_heroes:
        nombre = heroe.get("nombre")
        mensaje = nombre
        print(mensaje)


#C Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
def imprimir_nombre_altura_de_heroes(lista_heroes: list[dict]):
    #recorre una lista y devuelve cada nombre de personaje con su altura mediante un str
    for heroe in lista_heroes:
        nombre = heroe.get("nombre")
        altura = heroe.get("altura")
        mensaje = ("Heroe: {0} \nTiene una altura de: {1} cm".format(nombre, round(float(altura), 1)))
        print(mensaje)



#D Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def heroe_mas_alto(lista_heroes: list):
    #devuelve el heroe mas alto en un mensaje
    mas_alto = 0
    nombre_heroe_mas_alto = ""
    for heroe in lista_heroes:
        if float(heroe.get("altura")) >= mas_alto:
            nombre_heroe_mas_alto = heroe.get("nombre")
    mensaje = "El heroe mas alto es: {0}\n".format(nombre_heroe_mas_alto)
    return print(mensaje)


#E Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def heroe_mas_enano(lista_heroes: list):
    #Encuentra el heroe mas bajo y retorna su nombre mediante un mensaje
    mas_bajo = float(lista_heroes[0]["altura"])
    nombre_heroe_mas_bajo = ""
    for heroe in lista_heroes:
        if float(heroe.get("altura")) <= mas_bajo:
            nombre_heroe_mas_bajo = heroe.get("nombre")
    mensaje = "El heroe mas bajo es: {0}\n".format(nombre_heroe_mas_bajo)
    return print(mensaje)


#F Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)

def altura_promedio_de_heroes(lista_heroes: list):
    suma_de_alturas = 0
    contador_de_personajes = 0
    for heroes in lista_heroes:
        suma_de_alturas += float(heroes.get("altura"))
        contador_de_personajes += 1
    promedio = suma_de_alturas / contador_de_personajes
    mensaje = "El promedio de altura en los heroes es: {}cm \n".format(round(promedio, 2))
    return print(mensaje)


#G Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
def identidad_heroes_bajo_y_alto(lista_heroes: list):
    mas_bajo = float(lista_heroes[0]["altura"])
    identidad_heroe_mas_bajo = ""
    for heroe in lista_heroes:
        if float(heroe.get("altura")) <= mas_bajo:
            identidad_heroe_mas_bajo = heroe.get("identidad")

    mas_alto = float(lista_heroes[0]["altura"])
    identidad_heroe_alto = ""
    for heroe in lista_heroes:
        if float(heroe.get("altura")) >= mas_alto:
            identidad_heroe_alto = heroe.get("identidad")
    mensaje = "La identidad del heroe mas bajo es: {0} \nY el la del heroe mas alto es: {1}\n".format(identidad_heroe_mas_bajo,identidad_heroe_alto)
    return print(mensaje)


#H Calcular e informar cual es el superhéroe más y menos pesado.
def heroe_menos_y_mas_pesado(lista_heroes: list):
    #itera la lista y devuelve el heroe mas pesado y el menos pesado
    menos_pesado = lista_heroes[0]["nombre"]
    menos_pesado_kilaje = float(lista_heroes[0]["peso"])
    mas_pesado = lista_heroes[0]["nombre"]
    mas_pesado_kilaje = float(lista_heroes[0]["peso"])
    for heroe in lista_heroes:
        if float(heroe.get("peso")) >= mas_pesado_kilaje:
            mas_pesado = heroe.get("nombre")
            mas_pesado_kilaje = float(heroe.get("peso"))
        if float(heroe.get("peso")) <= menos_pesado_kilaje:
            menos_pesado = heroe.get("nombre")
            menos_pesado_kilaje = float(heroe.get("peso"))
    mensaje = "El heroe mas pesado es {}\nY el menos pesado es {}".format(mas_pesado,menos_pesado)
    return print(mensaje)


#J Construir un menú que permita elegir qué dato obtener

def mostrar_menu(lista_heroes: list[dict]):
    """
    ejecuta el menu principal
    recibe la lista de heroes
    """
    menu =\
        """
        1 - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
        2 - Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
        3 - Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
        4 - Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
        5 - Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
        6 - Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
        7 - Calcular e informar cual es el superhéroe más y menos pesado.
        8 - Salir
        """
    while True:
        print(menu)
        opcion_elegida = input("Elija una opcion: ")

        match opcion_elegida:
            case "1":
                imprimir_nombre_personajes(lista_heroes)
            case "2":
                imprimir_nombre_altura_de_heroes(lista_heroes)
            case "3":
                heroe_mas_alto(lista_heroes)
            case "4":
                heroe_mas_enano(lista_heroes)
            case "5":
                altura_promedio_de_heroes(lista_heroes)
            case "6":
                identidad_heroes_bajo_y_alto(lista_heroes)
            case "7":
                heroe_menos_y_mas_pesado(lista_heroes)
            case "8":
                break
            case _:
                print("opcion incorrecta, elija entre 1 y 9")

mostrar_menu(lista_personajes)