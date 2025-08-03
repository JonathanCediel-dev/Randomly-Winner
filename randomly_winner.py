# importaciones externas
import customtkinter as ctk

# importaciones standard 
import os
import random
from tkinter import messagebox

# Detectar entorno gráfico
es_wayland = "WAYLAND_DISPLAY" in os.environ
es_x11 = "DISPLAY" in os.environ and os.environ["DISPLAY"] != ":0"

# Tamaños según entorno
if es_wayland:
    tam_fuente = 40
    tam_ventana = "700x500"
    print("Entorno: WSLg (Wayland)")
elif es_x11:
    tam_fuente = 40
    tam_ventana = "600x450"
    print("Entorno: X11 (VcXsrv / GWSL)")
else:
    tam_fuente = 25
    tam_ventana = "550x400"
    print("No se detectó el entorno gráfico")

# Configuración de estilo
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# Lista de participantes
lista_participantes = []

# Crear ventana
ventana = ctk.CTk()
ventana.geometry(tam_ventana)
ventana.title("Seleccionar Ganador Aleatorio")

# Función para agregar un nombre a la lista de participantes
def agregar_participante():
    nombre = entrada.get().strip()
    if nombre:
        lista_participantes.append(nombre)
        entrada.delete(0, ctk.END)
        lista_caja.configure(state="normal") # se pone en modo editable
        lista_caja.insert("end", f"{nombre}\n") # se inserta el nombre en la caja con salto de linea al final
        lista_caja.configure(state="disabled") # se vuelve a bloquear la caja para no poder editarla directamente
    else:
        messagebox.showwarning("Campo vacío", "Debes ingresar un nombre.")

# Función para elegir un ganador aleatorio
def escoger_ganador():
    if lista_participantes:
        ganador = random.choice(lista_participantes)
        messagebox.showinfo("Ganador", f"¡El ganador es: {ganador}!")
    else:
        messagebox.showwarning("Sin participantes", "Agrega al menos un nombre primero.")

# Widgets // las variables ventana y tam_fuente se encuentran definidas a partir de la linea 14 luego de detectar el entorno gráfico
entrada = ctk.CTkEntry(ventana, placeholder_text="Escribe el nombre", font=("Arial", tam_fuente), width=400, height=50)
entrada.pack(pady=20)

boton_agregar = ctk.CTkButton(ventana, text="Agregar Participante", font=("Arial", tam_fuente), command=agregar_participante, width=300, height=50)
boton_agregar.pack(pady=10)

lista_caja = ctk.CTkTextbox(ventana, width=500, height=150, font=("Arial", tam_fuente - 10))
lista_caja.pack(pady=20)
lista_caja.configure(state="disabled")

boton_ganador = ctk.CTkButton(ventana, text="Elegir Ganador", font=("Arial", tam_fuente + 2), command=escoger_ganador, width=300, height=60)
boton_ganador.pack(pady=10)

ventana.mainloop()