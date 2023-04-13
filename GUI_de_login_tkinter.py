import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

ventana = tk.Tk()
ventana.geometry('300x130')
ventana.title('Login')
ventana.iconbitmap('icono.ico')
ventana.resizable(0,0) # se bloquea la ventana para que no cambie el tamaño

# Configuramos el grid

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=3)

entrada1 = ttk.Entry(ventana, width=30)
entrada1.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

entrada2 = ttk.Entry(ventana, width=30)
entrada2.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
entrada2.config(show='*')

#Etiqueta o Label
etiqueta1 = tk.Label(ventana, text='Usuario: ')
etiqueta1.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)

etiqueta2 = tk.Label(ventana, text='Password: ')
etiqueta2.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

def login():
    #mensaje1 = entrada1.get()
    #mensaje2 = entrada2.get()
    #messagebox.showinfo('Datos Login', 'Usuario: ' + mensaje1 + ', Password: ' + mensaje2)
    messagebox.showinfo('Datos Login', f'Usuario: {entrada1.get()}, Password: {entrada2.get()}')

# Defninimos dos botones
boton1 = ttk.Button(ventana, text='Login', command=login)
boton1.grid(row=3, column=0, columnspan=2)

ventana.mainloop()