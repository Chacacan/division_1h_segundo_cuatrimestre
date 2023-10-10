# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

NOMBRE = "" # Nombre del alumno

"""
#Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar 
    en la bolsa de valores.:

A) Para ello deberás programar el botón  para poder cargar 10 operaciones de compra 
    con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    Son 10 datos

B) Al presionar el botón mostrar 
    
    Informe 1 - Se deberán listar todos los datos de los usuarios y su posición en la lista (por terminal) 

# IMPORTANTE:
Del punto C solo deberá realizar SOLAMENTE 2 informes. 
(PRESUPONER QUE CADA CLIENTE INGRESADO ES UN CLIENTE DISTINTO, NINGUNO SE REPITE, 
no es necesario validar que no haya nombres repetidos)

Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 2 - Tome el último número de su DNI Personal (Ej 4) 
        y realice ese informe (Ej, Realizar informe 4)

    Informe 3 - Tome el último número de su DNI Personal (Ej 4), 
        y restarle al número 9 (Ej 9-4 = 5). En caso de que su DNI 
        finalice con el número 0, deberá realizar el informe 9.

    Realizar los informes correspondientes a los números obtenidos. 
        EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Tipo de instrumento que menos se operó en total.
    #! 1) - Tipo de instrumento que más se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion de la persona que menos BONOS compro
    #! 6) - Nombre y posicion del usuario que invirtio menos dinero
    #! 7) - Nombre y posicion del usuario que mas cantidad de instrumentos compró
    #! 8) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 9) - Promedio de cantidad de instrumentos  MEP vendidos en total
"""

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Bolsa de valores de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Bolsa de valores {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)


        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar cartas", command=self.btn_cargar_datos_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")
        
        #PUEDE MODIFICAR LOS DATOS A SU ANTOJO, A EFECTOS DE REALIZAR PRUEBAS
        self.lista_nombre = ["Lisandro", "Carlos", "Facu", "Carolina", "Rocio", "Agustin", "Beti", "Paloma", "Raquel", "Daniel"]
        self.lista_monto = [15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000]
        self.lista_instrumento = ["CEDEAR", "CEDEAR", "MEP", "MEP" , "MEP", "MEP", "BONOS", "BONOS", "BONOS", "CEDEAR"]
        self.lista_cantidad_de_instrumento = [5,9,15,6,21,25,36,7,6,99]

    def btn_mostrar_todos_on_click(self):
        print(f"Nombre: Monto: Tipo: Cantidad de instrumentos: Lugar en la lista:")
        for indice in range(10):
            print(f"{self.lista_nombre[indice]} {self.lista_monto[indice]} {self.lista.tipo[indice]} {self.lista_cantidad_de_instrumento[indice]} {indice}")

    def btn_mostrar_informe_1(self):
        #! 0) - Tipo de instrumento que menos se operó en total.
        acumulador_cedear = 0
        acumulador_mep = 0
        acumulador_bono = 0

        largo_de_la_lista = len(self.lista_cantidad_de_instrumento)
        for indice in range(largo_de_la_lista):
            match self.lista_tipo[indice]:
                case "Cedear":
                    acumulador_cedear += self.lista_cantidad_de_instrumento[indice]

                case "MEP":
                    acumulador_mep += self.lista_cantidad_de_instrumento[indice]

                case _:
                    acumulador_bono += self.lista_cantidad_de_instrumento[indice]
            
            
            
            """if self.lista_tipo [indice] == "CEDEAR":
                acumulador_cedear += self.lista_cantidad_de_instrumento[indice]
            elif self.lista_tipo[indice] == "MEP":
                acumulador_mep += self.lista_cantidad_de_instrumento[indice]
            else:
                acumulador_bono += self.lista_cantidad_de_instrumento[indice]
        """

        if acumulador_bono < acumulador_cedear and acumulador_bono < acumulador_mep:
            instrumento_menos_operado = "bono"
        elif acumulador_cedear < acumulador_mep:
            instrumento_menos_operado = "Cedear"
        else:
            instrumento_menos_operado = "MEP"
        print(f"{instrumento_menos_operado}")

    def btn_mostrar_informe_2(self):
        #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
        contador_usuarios = 0
        for i in range(len(self.lista_cantidad_de_instrumento)):
            if self.lista_instrumento [i] == "MEP":
                if self.lista_cantidad_de_instrumento [i] > 50 and self.lista_cantidad_de_instrumento [i] < 200:
                    contador_usuarios += 1
        print(contador_usuarios)
    def btn_mostrar_informe_3(self):
        #! 3) - Cantidad de usuarios que no compraron CEDEAR
        contador_no_compador = 0
        for i in range(0, len(self.lista_de_nombres)):
            if self.lista_tipo[i] == "CEDEAR" :
                contador_no_compador += 1
        print(f"La cantidad de no compradores es {contador_no_compador}")

    def btn_cargar_datos_on_click(self):
        #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()