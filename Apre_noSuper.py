import tkinter as tk
from tkinter import messagebox
import random
import webcolors

# Función para calcular una mezcla de colores primarios aproximada al color deseado
def calcular_mezcla(rgb):
    r, g, b = rgb

    # Normalizamos los valores RGB para obtener los porcentajes de los colores primarios
    total = r + g + b
    if total == 0:
        return [{"rojo": 0, "amarillo": 0, "azul": 0} for _ in range(3)]  # Caso borde: color negro

    rojo_pct = round((r / total) * 100)
    amarillo_pct = round((g / total) * 100)
    azul_pct = round((b / total) * 100)

    # Generamos 3 variaciones aleatorias de la mezcla
    return [
        {
            "rojo": min(100, max(0, rojo_pct + random.randint(-5, 5))),
            "amarillo": min(100, max(0, amarillo_pct + random.randint(-5, 5))),
            "azul": min(100, max(0, azul_pct + random.randint(-5, 5)))
        }
        for _ in range(3)
    ]

# Función para encontrar el color RGB más cercano a partir del nombre ingresado
def obtener_rgb_color(nombre_color):
    try:
        return webcolors.name_to_rgb(nombre_color)
    except ValueError:
        messagebox.showerror("Error", f"No reconozco el color '{nombre_color}'. Prueba con otro nombre.")
        return None

def mostrar_opciones():
    nombre_color = entrada_color.get().strip().lower()
    rgb = obtener_rgb_color(nombre_color)

    if rgb:
        opciones_actuales[:] = calcular_mezcla(rgb)  # Actualiza la lista de opciones
        actualizar_opciones()

def actualizar_opciones():
    for widget in canvas_opciones.winfo_children():
        widget.destroy()  # Limpia las opciones anteriores

    for idx, opcion in enumerate(opciones_actuales):
        r = int(opcion['rojo'] * 2.55)
        g = int(opcion['amarillo'] * 2.55)
        b = int(opcion['azul'] * 2.55)

        # Nos aseguramos de que los valores estén en el rango (0-255)
        r, g, b = max(0, min(r, 255)), max(0, min(g, 255)), max(0, min(b, 255))
        color_hex = f'#{r:02x}{g:02x}{b:02x}'

        # Crear un botón de color con la mezcla generada
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

opciones_actuales = []

tk.Label(ventana, text="¿Qué color deseas?").pack(pady=10)
entrada_color = tk.Entry(ventana, width=30)
entrada_color.pack(pady=5)

btn_buscar = tk.Button(ventana, text="Buscar Opciones", command=mostrar_opciones)
btn_buscar.pack(pady=5)

canvas_opciones = tk.Frame(ventana)
canvas_opciones.pack(pady=10)

ventana.mainloop()
