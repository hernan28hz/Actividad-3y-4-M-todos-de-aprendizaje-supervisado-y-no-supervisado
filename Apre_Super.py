import tkinter as tk
from tkinter import messagebox
import random

# Base de datos de colores con sus porcentajes de mezcla
colores = {
    "naranja atardecer": [
        {"rojo": 60, "amarillo": 40, "azul": 0},
        {"rojo": 55, "amarillo": 45, "azul": 0},
        {"rojo": 65, "amarillo": 35, "azul": 0}
    ],
    "verde menta": [
        {"rojo": 10, "amarillo": 60, "azul": 30},
        {"rojo": 5, "amarillo": 65, "azul": 30},
        {"rojo": 0, "amarillo": 70, "azul": 30}
    ],
    "púrpura real": [
        {"rojo": 50, "amarillo": 0, "azul": 50},
        {"rojo": 45, "amarillo": 5, "azul": 50},
        {"rojo": 55, "amarillo": 0, "azul": 45}
    ]
    
}

# Variable global para almacenar opciones seleccionadas
opciones_actuales = []

def mostrar_opciones():
    global opciones_actuales
    color_deseado = entrada_color.get().strip().lower()
    
    if color_deseado in colores:
        opciones_actuales = random.sample(colores[color_deseado], 3)  # Selecciona 3 opciones aleatorias
        actualizar_opciones()
    else:
        messagebox.showerror("Error", "Ese color no está disponible en la base de datos.")

def actualizar_opciones():
    for widget in canvas_opciones.winfo_children():
        widget.destroy()  # Limpia el canvas para nuevas opciones

    for idx, opcion in enumerate(opciones_actuales):
        # Convertimos los porcentajes en valores RGB (0-255)
        r = int(opcion['rojo'] * 2.55)
        g = int(opcion['amarillo'] * 2.55)
        b = int(opcion['azul'] * 2.55)
        color_hex = f'#{r:02x}{g:02x}{b:02x}'

        # Crear un botón colorido para cada opción
        boton = tk.Button(canvas_opciones, bg=color_hex, width=20, height=2, 
                        command=lambda idx=idx: seleccionar_opcion(idx))
        boton.grid(row=idx, column=0, padx=10, pady=5)

def seleccionar_opcion(idx):
    opcion = opciones_actuales[idx]
    mensaje = (f"Para lograr ese color mezcla:\n"
                f"Rojo: {opcion['rojo']}%\n"
                f"Amarillo: {opcion['amarillo']}%\n"
                f"Azul: {opcion['azul']}%")
    messagebox.showinfo("Instrucciones", mensaje)

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Mezclador de Colores")

tk.Label(ventana, text="¿Qué color deseas?").pack(pady=10)
entrada_color = tk.Entry(ventana, width=30)
entrada_color.pack(pady=5)

btn_buscar = tk.Button(ventana, text="Buscar Opciones", command=mostrar_opciones)
btn_buscar.pack(pady=5)

# Canvas para mostrar las opciones como colores
canvas_opciones = tk.Frame(ventana)
canvas_opciones.pack(pady=10)

ventana.mainloop()
