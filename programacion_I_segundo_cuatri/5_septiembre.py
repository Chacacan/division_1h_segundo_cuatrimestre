# """ 1 Crea un diccionario que represente los días de la semana, donde las claves son los nombres de los días y los valores son los números correspondientes (por ejemplo, {"lunes": 1, "martes": 2, ...}). Imprime el valor correspondiente al día "miércoles".
# """

# dias_de_la_semana = {
#     "lunes": 1,
#     "martes": 2,
#     "miercoles": 3,
#     "jueves": 4,
#     "viernes": 5,
#     "sabado": 6,
#     "domingo": 7

#     }

# clave_a_buscar = "miercoles"
# print(dias_de_la_semana.get(clave_a_buscar, "La clave {0} no existe".format(clave_a_buscar)))
# print(dias_de_la_semana.get(clave_a_buscar, f"La clave {clave_a_buscar} no existe"))#las dos formas imprimen lo mismo

# """ 2 Crea un diccionario que represente los meses del año, donde las claves son los nombres de los meses y los valores son sus números correspondientes (por ejemplo, {"enero": 1, "febrero": 2, ...}). Imprime el número correspondiente al mes "julio".

# """

# meses_del_anho = {
#     "enero": 1,
#     "febrero": 2,
#     "marzo": 3,
#     "abril": 4,
#     "mayo": 5,
#     "junio": 6,
#     "julio": 7,
#     "agosto": 8,
#     "septiembre": 9,
#     "octubre": 10,
#     "noviembre": 11,
#     "diciembre": 12
#     }

# numero_de_junio = meses_del_anho.get("junio", "Error 404")
# print(numero_de_junio)

# """ 3 Crea un diccionario que contenga la información de una película, como título, director y año de estreno. Luego, imprime el título de la película.
# """

# info_pelicula = {
#     "titulo": "Reliquias de la muerte I",
#     "director": "UTN Pirata",
#     "año": "2023"
# }

# titulo_de_la_pelicula = info_pelicula.get("titulo", "La clave tutylo no existe prro")
# print(titulo_de_la_pelicula)

# """ 4 Crea un diccionario que contenga la información de una dirección: nombre de la calle, altura, localidad, código postal, partido y provincia. Luego, imprime el nombre de la calle, seguido de su altura.
# """

# direccion = {
#     "nombre_calle": "calle falsa",
#     "altura": "123",
#     "localidad": "Springfield",
#     "partido": "Springfield",
#     "codigo_postal": "2525",
#     "provincia": "Simpsoniana"
# }

# nombre_de_calle = direccion.get("nombre_calle", "El nombre de la calle no fue definido")
# altura_direccion = direccion.get("altura", "La altura de la direccion no fue definida")

# dato_direccion = f"La calle es : {nombre_de_calle}\naltura: {altura_direccion}"
# print(dato_direccion)

# """ 5 Crea un diccionario que represente los continentes, donde las claves son los nombres de los continentes y los valores son los números correspondientes (por ejemplo, {"América": 1, "Europa": 2, ...}). Imprime el valor correspondiente al continente "África".
# """
# contienentes = {
#     "Asia" : 1,
#     "America" : 2,
#     "Africa" : 3,
#     "Antartida" : 4,
#     "Europa" : 5,
#     "Oceania" : 6
# }
# valor_del_pais = contienentes.get("Africa", "No existe dicho contienente")
# mensaje = "El valor del contienente es: {0}".format(valor_del_pais)
# print(mensaje)

# """ 6 Crea un diccionario que represente las estaciones del año, donde las claves son los nombres de las estaciones y los valores son los números correspondientes (por ejemplo, {"primavera": 1, "verano": 2, ...}). Imprime el valor correspondiente a la estación "invierno".
# """
# estaciones_del_anho = {
#     "Primavera" : 1,
#     "Verano" : 2,
#     "Otoño" : 3,
#     "Invierno" : 4
# }
# valor_de_estacion = estaciones_del_anho.get("Invierno", "No existe la estacion")
# mensaje = "El valor de la estación es: {0}".format(valor_de_estacion)
# print(mensaje)

# """ 7 Crea un diccionario que contenga la información de una canción: título, artista y duración. Luego, imprime la duración de la canción.
# """
# cancion = {
#     "Titulo" : "las ganzadas de juanito",
#     "Artista" : "Juanito Pachorra",
#     "Duracion" : 3.58
# }

# duracion_de_la_cancion = cancion.get("Duracion", "No existe rey")
# mensaje = "La duracion de la cancion es: {0} minutos".format(duracion_de_la_cancion)
# print(mensaje)

# """ 8 Crea un diccionario que represente las edades de varias personas, donde las claves son los nombres de las personas y los valores son sus edades. Imprime la edad de la persona más joven.
# """
# personas = {
#     "Valentin" : 19,
#     "Marcia" : 33,
#     "Mauricio" : 22,
#     "Rocio" : 25
# }
# menor_edad = 5000000
# for edad in personas.values():
#     if edad < menor_edad:
#         menor_edad = edad

# print(menor_edad)


# """ 9 Crea un diccionario que contenga las capitales de los países de América del Sur. Luego, pide al usuario que ingrese el nombre de un país y muestra su capital correspondiente.
# """

# capitales_america_del_sul = {
#     "Argentina": "Buenos aires",
#     "Brasil": "Brasilia",
#     "Uruguay": "Montevideo",
#     "Paraguay": "Asuncion",
#     "Bolibia": "La paz"
# }

# nombre_de_pais = input("Ingrese el nombre de un pais de ADS: ").capitalize()

# if not nombre_de_pais in capitales_america_del_sul.keys():
#     mensaje = f"El pais {nombre_de_pais} no esta presente en el diccionario"
# else:
#     capital_seleccionada = capitales_america_del_sul.get(nombre_de_pais)
#     mensaje = f"La capital de {nombre_de_pais} es {capital_seleccionada}!"
# print(mensaje)

# """ 10 Crea un diccionario que represente las notas de un examen de varios estudiantes, donde las claves son los nombres de los estudiantes y los valores son sus notas. Imprime el promedio de las notas.
# """
# varios_estudiantes = {
#     "Ramiro": 9,
#     "Romualdo" : 7,
#     "Roberto" : 4,
#     "Ricardo" : 6
# }
# total_de_notas_sumadas = 0
# cantidad_de_alumnos = 0
# for nota in varios_estudiantes.values():
#     total_de_notas_sumadas += nota
#     cantidad_de_alumnos += 1

# promedio_de_las_notas_por_alumno = total_de_notas_sumadas / cantidad_de_alumnos
# mensaje = "El promedio de las notas de los alumnos es: {0}".format(promedio_de_las_notas_por_alumno)
# print(mensaje)

# """11 Crea un diccionario que represente una lista de tareas por hacer. Cada clave del diccionario debe ser el nombre de una tarea y cada valor debe ser su estado (los estados son:  pendiente, en proceso, completada). Imprimir todas las tareas seguido de su estado
# """
# lista_de_tareas = {
#     "trabajar" : "completada",
#     "estudiar" : "pendiente",
#     "cocinar" : "pendiente",
#     "dormir" : "pendiente"
# }
# for clave, valor in lista_de_tareas.items():
#     mensaje = "la tarea {0} esta: {1}".format(clave, valor)
#     print(mensaje)

# """12 Crea un diccionario que represente una lista de las compras. Cada clave del diccionario debe ser el nombre de un producto y cada valor debe ser su cantidad. Pedir al usuario que ingrese el nombre del producto e imprimir la cantidad
# """
# lista_de_compras = {
#     "Azucar" : 10,
#     "Yerba" : 2,
#     "Fideo" : 5,
#     "Jugo" : 10
# }
# cantidad_de_producto = input("ingrese el nombre del producto: ").capitalize()

# for clave, valor in lista_de_compras.items():
#     if clave == cantidad_de_producto:
#         mensaje = "El producto tiene {0} unidades".format(valor)
#         print(mensaje)
#     else:
#         mensaje = "El producto no se encuentra"
#         print(mensaje)
#         break


# """13 Crea un diccionario que contenga el nombre y el nivel de dificultad de varios juegos de mesa. Luego, pedirle al usuario un nivel de dificultad, buscar los que coinciden e imprimir sus nombres
# """

# info_juegos_de_mesa = {
#     "Monopoly": "Intermedio",
#     "Truco": "Facil",
#     "Canasta": "Facil",
#     "Poker": "Dificil"
# }

# nivel_de_dificultad = input("Ingrese el nivel de dificultad: ").capitalize()

# for clave, valor in  info_juegos_de_mesa.items():
#     if valor == nivel_de_dificultad:
#         print(clave)

# """14 Crea un diccionario que contenga el nombre como clave y el puntaje como valor de varios jugadores en un juego. Luego, pedirle al usuario el nombre del jugador y nuevo puntaje y actualizar el valor correspondiente en el diccionario.
# """

# jugadores = {
#     "Ramiro": 750,
#     "Romualdo" : 700,
#     "Roberto" : 400,
#     "Ricardo" : 600
# }

# seleccion_de_nombre = input("Ingrese el nombre de usuario para actualizar puntaje: ").capitalize()
# while not seleccion_de_nombre in jugadores:
#     seleccion_de_nombre = input("Ingrese correctamente el nombre de usuario para actualizar puntaje: ").capitalize()

# actualizar_puntaje = input("Ingrese el puntaje: ")
# while not actualizar_puntaje.isnumeric():
#     actualizar_puntaje = input("Ingrese el puntaje nuevamente: ")


# jugadores[seleccion_de_nombre] = (int(actualizar_puntaje))
# print(jugadores) 

# """15 Crea un diccionario que contenga el nombre y el sueldo de varios empleados. Luego, permite al usuario aumentar el sueldo de un empleado y actualizar el valor correspondiente en el diccionario.
# """
# empleados = {
#     "Ramiro": 250000,
#     "Romualdo" : 700000,
#     "Roberto" : 400000,
#     "Ricardo" : 600000
# }

# seleccion_de_nombre = input("Ingrese el nombre de usuario para actualizar sueldo: ").capitalize()
# while not seleccion_de_nombre in empleados:
#     seleccion_de_nombre = input("Ingrese correctamente el nombre de usuario para actualizar sueldo: ").capitalize()

# actualizar_sueldo = input("Ingrese el sueldo: ")
# while not actualizar_sueldo.isnumeric():
#     actualizar_sueldo= input("Ingrese el sueldo nuevamente: ")


# empleados[seleccion_de_nombre] = (int(actualizar_sueldo))
# print(empleados) 

# """16 Crea un diccionario que represente una lista de tareas pendientes, donde las claves son las tareas y los valores son "True" si están completadas y "False" si no lo están. Solicita al usuario el nombre de una tarea y modifica el valor para marcarla como completada. Imprimir el listado de tareas pendientes
# """

# lista_de_tareas = {
#     "Trabajar" : "True",
#     "Estudiar" : "False",
#     "Cocinar" : "True",
#     "Dormir" : "False"
# }

# actualizacion_de_tarea = input("Ingrese el nombre de la tarea para actualizar: ").capitalize()
# while not actualizacion_de_tarea in lista_de_tareas:
#     actualizacion_de_tarea = input("Ingrese correctamente el nombre de la tarea para actualizar: ").capitalize()

# modificar_estado_de_tarea = input("ingrese el estado de la tarea ingresada: ").capitalize()
# while modificar_estado_de_tarea != "True" and modificar_estado_de_tarea != "False":
#     modificar_estado_de_tarea = input("ingrese correctamente el estado de la tarea ingresada: ").capitalize()

# if modificar_estado_de_tarea == "True":
#     lista_de_tareas[actualizacion_de_tarea] = (modificar_estado_de_tarea)
# if modificar_estado_de_tarea == "False":
#     lista_de_tareas[actualizacion_de_tarea] = (modificar_estado_de_tarea)

# print("lista de tareas pendientes: ")
# for clave in lista_de_tareas:
#     if lista_de_tareas[clave] == "False":
#         print("{0}".format(clave))

# """17 Crea un diccionario que represente las películas de un cine, donde las claves son los nombres de las películas y los valores son los horarios correspondientes. Modifica el horario de la película "Avengers: Endgame" a las 19:30.
# """

# lista_de_peliculas = {
#     "One piece" : "15:30",
#     "Avengers" : "20:30",
#     "Shrek" : "22:50"
# }
# print(lista_de_peliculas)
# lista_de_peliculas["Avengers"]= ("19:30")
# print(lista_de_peliculas)

# """18 Crea un diccionario que represente los juegos de una consola, donde las claves son los nombres de los juegos y los valores son las puntuaciones correspondientes. Solicita al usuario el nombre de un juego y luego su puntuación, si el juego no existe agregarlo y si existe actualizar su puntuación 
# """

# juegos = {
#     "Super mario" : 3500,
#     "Final fight" : 5000,
#     "Nekketsu Kakutou Densetsu" : 6000
# }

# actualizacion_de_juego = input("Ingrese el nombre del juego para actualizar: ").capitalize()
# if actualizacion_de_juego in juegos:
#     modificar_puntaje_de_juego = input("ingrese puntuacion nueva: ")
#     while not modificar_puntaje_de_juego.isnumeric():
#         modificar_puntaje_de_juego= input("Ingrese correctamente el puntaje: ")
#     juegos[actualizacion_de_juego] = (int(modificar_puntaje_de_juego))
# else:
#     puntuacion_nuevo_juego = input("Ingrese su puntuacion en el nuevo juego: ")
#     juegos[actualizacion_de_juego] = (int(puntuacion_nuevo_juego))

# print(juegos)

# """19 Crea un diccionario que represente las temperaturas de una ciudad durante una semana, donde las claves son los días de la semana y los valores son las temperaturas correspondientes. Calcula la temperatura promedio de la semana.
# """


# dias_de_la_semana_y_temperaturas = {
#     "lunes": 15,
#     "martes": 20,
#     "miercoles": 13,
#     "jueves": 24,
#     "viernes": 15,
#     "sabado": 26,
#     "domingo": 17
#     }
# suma_de_temperaturas = 0
# for valor in dias_de_la_semana_y_temperaturas.values():
#     suma_de_temperaturas += valor

# temperatura_promedio_de_la_semana = round(suma_de_temperaturas / 7,2)
# print("la temperatura promedio de la semana es: {0}°C".format(temperatura_promedio_de_la_semana))

# """20 Crea un diccionario que represente los asientos de un avión, donde las claves son los números de asientos y los valores son "True" si están ocupados y "False" si no lo están. Solicita al usuario un número de asiento y modifica su valor para marcarlo como ocupado. Luego imprimí la lista de asientos libres
# """
# asientos_de_avion = {
#     "1" : "true",
#     "2" : "false",
#     "3" : "false",
#     "4" : "true",
#     "5" : "false",
#     "6" : "true"
# }
# solicitud_de_asiento = input("ingrese el numero de asiento: ")
# while solicitud_de_asiento.isalpha() or int(solicitud_de_asiento) > len(asientos_de_avion) or asientos_de_avion[solicitud_de_asiento] == "true":
#     solicitud_de_asiento = input("vuelva a ingresar otro numero asiento ya que el mismo se encuentra ocupado: ")

# asientos_de_avion[solicitud_de_asiento] = ("true")
# for clave in asientos_de_avion:
#     print("\n asiento: {0} = {1}".format(clave, asientos_de_avion[clave]))

# """21 Crea un diccionario que represente los gastos de una persona en diferentes categorías, donde las claves son los nombres de las categorías y los valores son los gastos correspondientes. Calcula el total de gastos de la persona.
# """
# gastos_del_mes = {
#     "Ropa" : 10000,
#     "Comida" : 50000,
#     "Transporte" : 20000,
#     "Limpieza" : 10000,
#     "Servicios" : 20000
# }
# gasto_total_del_mes = 0
# for valor in gastos_del_mes:
#     gasto_total_del_mes += gastos_del_mes[valor]
# print("El total del gasto del mes es: ${0}".format(gasto_total_del_mes))

# """23 Crea un diccionario que represente los contactos de un teléfono, donde las claves son los nombres de las personas y los valores son los números de teléfono correspondientes. Solicitar al usuario el nombre de un contacto: agregarlo al diccionario en caso de que no exista. En caso de que exista modificar el número de teléfono del contacto.
# """
# contactos_de_telefono = {
#     "Carolina" : 1133445533,
#     "Carlos" : 1133445544,
#     "Ricardo" : 1133445555,
#     "Romina" : 1133445577
# }
# solicitud_de_contacto = input("Ingresa el nombre del contacto: ").capitalize()
# if solicitud_de_contacto in contactos_de_telefono:
#     solicitud_de_numero_nuevo = input("ingrese el nuevo numero telefonico de 10 digitos: ")
#     while solicitud_de_numero_nuevo.isalpha() or len(solicitud_de_numero_nuevo) < 9:
#         solicitud_de_numero_nuevo = input("Eror vuelva a ingresar el nuevo numero telefonico de 10 digitos: ")
# else:
#     solicitud_de_numero_nuevo = input("ingrese el nuevo numero telefonico de 10 digitos: ")
#     while solicitud_de_numero_nuevo.isalpha() or len(solicitud_de_numero_nuevo) < 9:
#         solicitud_de_numero_nuevo = input("Eror vuelva a ingresar el nuevo numero telefonico de 10 digitos: ")
# contactos_de_telefono[solicitud_de_contacto] = (solicitud_de_numero_nuevo)

# print("Contactos actuales: ")
# for valor in contactos_de_telefono:
#     print("\nNombre: {0} Numero: {1}".format(valor, contactos_de_telefono[valor]))

