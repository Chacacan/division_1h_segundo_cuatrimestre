def formatear_puntaje(puntaje: str) -> str:
    puntaje = puntaje.zfill(4)
    return puntaje

def formatear_nombre_jugador(nombre: str) -> str:
    texto_lista = nombre.split()
    texto_limpio = texto_lista[0]
    nombre = texto_limpio.strip().capitalize()
    return nombre