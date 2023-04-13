import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de grid')
ventana.iconbitmap('icono.ico')

# Configuramos el grid
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=5)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

# Metodos de los eventos
def evento1():
    boton1.config(text='Boton 1 presionado')

def evento2():
    boton2.config(text='Boton 2 presionado')

def evento3():
    boton3.config(text='Boton 3 presionado')

def evento4():
    boton4.config(text='Boton 4 presionado', fg='blue', relief=tk.GROOVE, bg='yellow')

# Defninimos dos botones
boton1 = ttk.Button(ventana, text='Boton 1', command=evento1)
boton1.grid(row=0, column=0, sticky='NSWE', padx=40, pady=60, ipadx=20, ipady=50, columnspan=2, rowspan=2) # el grid es tipo (fila,columna)

# N(arriba), E(derecha), S(abajo), W(izquierda) para esto se usa sticky
boton2 = ttk.Button(ventana, text='Boton 2', command=evento2)
#boton2.grid(row=0, column=1, sticky='NSWE') # el grid es tipo (fila,columna)

boton3 = ttk.Button(ventana, text='Boton 3', command=evento3)
#boton3.grid(row=1, column=0, sticky='NSWE') # el grid es tipo (fila,columna)

boton4 = tk.Button(ventana, text='Boton 4', command=evento4)
#boton4.grid(row=1, column=1, sticky='NSWE') # el grid es tipo (fila,columna)

ventana.mainloop()