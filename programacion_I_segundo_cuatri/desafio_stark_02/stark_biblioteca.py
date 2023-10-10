from data_stark import lista_personajes
import os 

#1 Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
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
def obtener_nombre(heroe: dict)-> str:
    #imprime el nombre del heroe seleccionado
    #devuelve un print por consola
    nombre = "Nombre: {0}".format(heroe["nombre"])
    return nombre
#obtener_nombre(lista_personajes[0])

def imprimir_dato(un_string: str) -> None:
    #imprime el dato que recibe 
    print(un_string)

def stark_imprimir_nombre_heroes(lista_heroes: list):
    if not lista_heroes:
        return -1
    else:
        for heroe in lista_heroes:
            imprimir_dato(obtener_nombre(heroe))
#star_imprimir_nombre_heroes(lista_personajes)


#2 Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def obtener_nombre_y_dato(heroe: dict,key: str) -> str:
    return  "Nombre: {0} | {1}: {2}".format(heroe["nombre"], key, heroe[key])

#print(obtener_nombre_y_dato(lista_personajes[5],"fuerza"))

def stark_imprimir_nombre_alturas(lista_heroes: list):
    if not lista_heroes:
        return -1
    else:
        for heroe in lista_heroes:
            imprimir_dato(obtener_nombre_y_dato(heroe,"altura"))

#stark_imprimir_nombre_alturas(lista_personajes)

def calcular_max(lista_heroes: list, key: str) -> dict:
    valor_maximo = None
    for heroe in lista_heroes:
        if valor_maximo == None or float(valor_maximo.get(key)) <= float(heroe.get(key)):
            valor_maximo = heroe
    return valor_maximo
#print(calcular_max(lista_personajes,"fuerza"))

def calcular_min(lista_heroes: list, key: str) -> dict:
    valor_minimo = None
    for heroe in lista_heroes:
        if valor_minimo == None or float(valor_minimo.get(key)) >= float(heroe.get(key)):
            valor_minimo = heroe
    return valor_minimo
#print(calcular_min(lista_personajes,"peso"))

def calcular_max_min_dato(lista_heroes: list, max_o_min: str, key: str ) -> dict:
    if max_o_min == "maximo":
        return calcular_max(lista_heroes,key)
    if max_o_min == "minimo":
        return calcular_min(lista_heroes,key)
    else:
        None
#print(calcular_max_min_dato(lista_personajes,"minimo","altura"))

#imprimir_dato()
#obtener_nombre_y_dato()
#calcular_max_min_dato()
def stark_calcular_imprimir_heroe(lista_heroes: list, max_o_min: str, key: str):
    if not lista_heroes:
        return -1
    else:
        match max_o_min:
            case "maximo":
                return imprimir_dato("Mayor {0}: {1}".format(key,obtener_nombre_y_dato(calcular_max_min_dato(lista_heroes,max_o_min,key),key)))
            case "minimo":
                return imprimir_dato("Menor {0}: {1}".format(key,obtener_nombre_y_dato(calcular_max_min_dato(lista_heroes,max_o_min,key),key)))
            case _:
                return imprimir_dato("No introdujo un maximo o minimo")
#stark_calcular_imprimir_heroe(lista_personajes,"maximo","altura")

def sumar_dato_heroe(lista_heroes: list, key: str):
    sumar = 0
    for heroe in lista_heroes:
        if isinstance(heroe, dict) or heroe.get(key, False):
            sumar += float(heroe.get(key))
    return sumar
#print(sumar_dato_heroe(lista_personajes,"peso"))

def dividir(dividendo: float, divisor: float):
    if divisor != 0:
        return dividendo / divisor
    else:
        return 0
#print(dividir(10,5))

def calcular_promedio(lista_heroes: list, key: str):
    promedio = dividir(sumar_dato_heroe(lista_heroes,key),len(lista_heroes))
    return promedio
#print(calcular_promedio(lista_personajes,"peso"))

def stark_calcular_imprimir_promedio_altura(lista_heroes):
    if not lista_heroes:
        retur -1
    else:
        imprimir_dato(calcular_promedio(lista_heroes,"altura"))
#stark_calcular_imprimir_promedio_altura(lista_personajes)

def imprimir_menu():
    menu =\
    """
    1 Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
    2 Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
    3 Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    4 Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    5 Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
    6 Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
    7 Calcular e informar cual es el superhéroe más y menos pesado.
    10 salir
    """
    imprimir_dato(menu)
#imprimir_menu()

def validar_entero(key: str) -> bool:
    return key.isnumeric()

def stark_menu_principal():
    imprimir_menu()
    seleccion_numero = input("Ingrese la opcion requerida: ") 
    if validar_entero(seleccion_numero):
        seleccion_numero = int(seleccion_numero)
    else:
        seleccion_numero = -1
    return seleccion_numero

def limpiar_consola():
    _= input("\npresione una tecla para continuar... ")
    if os.name in ['ce','nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')


def stark_marvel_app(lista_heroes):
    while True:
        opcion_elegida = stark_menu_principal()
        if opcion_elegida == 1:
            stark_imprimir_nombre_heroes(lista_heroes)
        elif opcion_elegida == 2:
            stark_imprimir_nombre_alturas(lista_heroes)
        elif opcion_elegida == 3:
            stark_calcular_imprimir_heroe(lista_heroes,"maximo","altura")
        elif opcion_elegida == 4:
            stark_calcular_imprimir_heroe(lista_heroes,"minimo","altura")
        elif opcion_elegida == 5:
            stark_calcular_imprimir_promedio_altura(lista_heroes)
        elif opcion_elegida == 6:
            stark_calcular_imprimir_heroe(lista_heroes,"maximo","altura")
            stark_calcular_imprimir_heroe(lista_heroes,"minimo","altura")
        elif opcion_elegida == 7:
            stark_calcular_imprimir_heroe(lista_heroes,"maximo","peso")
            stark_calcular_imprimir_heroe(lista_heroes,"minimo","peso")
        elif opcion_elegida == 8:
            imprimir_dato("Gracias por la visita!")
            break
        else:
            imprimir_dato("opcion incorrecta, elija entre 1 y 8")
            
        limpiar_consola()
