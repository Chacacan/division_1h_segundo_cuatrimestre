from biblioteca_stark01 import *

def main_app(lista_heroes: list[dict]):
    """
    ejecuta el menu principal
    recibe la lista de heroes
    """

    while True:
        opcion_elegida = mostrar_menu()
        match opcion_elegida:
            case "1":
                personajes_femeninos(lista_heroes)
            case "2":
                heroe_m_mas_alto = heroe_masculino_mas_alto(personajes_masculinos_lista)
                print("El heroe masculino mas alto es: {0}".format(heroe_m_mas_alto))
            case "3":
                heroe_mas_alto_fem = heroe_femenino_mas_alto(personajes_femeninos_lista)
                print("El heroe femenino mas alto es: {0}".format(heroe_mas_alto_fem))
            case "4":
                heroe_f_mas_bajo = heroe_mas_bajo_femenino(personajes_femeninos_lista)
                print("El heroe femenino mas bajo es: {0}".format(heroe_f_mas_bajo))
            case "5":
                heroe_m_mas_bajo = heroe_mas_bajo_masculino(personajes_masculinos_lista)
                print("El heroe masculino mas bajo es: {0}".format(heroe_m_mas_bajo))
            case "6":
                promedio_de_alturas = altura_promedio_masculinos(lista_heroes)
                print("El promedio de alturas masculino es: {0}cm".format(promedio_de_alturas))
            case "7":
                promedio_de_alturas_f = altura_promedio_femeninos(lista_heroes)
                print("El promedio de alturas femeninos es: {0}cm".format(promedio_de_alturas_f))
            case "8":
                informe = informe_de_items_C_F(heroe_masculino_mas_alto(personajes_masculinos_lista),heroe_mas_bajo_femenino(personajes_femeninos_lista))
                print(informe)
            case "9":
                contador_de_personajes_por_color_ojos(cantidad_heroes_por_color_ojos(lista_heroes))
            case "10":
                contador_de_personajes_por_color_pelo(cantidad_heroes_por_color_pelo(lista_heroes))
            case "11":
                contador_de_personajes_por_inteligencia(cantidad_heroes_por_tipo_de_inteligencia(lista_heroes))
            case "12":
                recorrer_diccionario_para_imprimir_color_ojos(cantidad_heroes_por_color_ojos(lista_heroes))
            case "13":
                print(recorrer_diccionario_para_imprimir_color_pelo(cantidad_heroes_por_color_pelo(lista_heroes)))
            case "14":
                recorrer_diccionario_para_imprimir_lista_inteligencia(cantidad_heroes_por_tipo_de_inteligencia(lista_heroes))
            case "15":
                break
            case _:
                print("opcion incorrecta, elija entre 1 y 15")
        limpiar_consola()