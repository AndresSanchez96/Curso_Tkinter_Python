import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de grid')
ventana.iconbitmap('icono.ico')


entrada_var1 = tk.StringVar(value='Valor por default')
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada_var1)
entrada1.grid(row=0, column=0)

#Etiqueta o Label
etiqueta1 = tk.Label(ventana, text='Aqui se mostrara el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)

def enviar():
    # recuperamos la informacion a partir de la variable asociada con la caja de texto
    #boton1.config(text=entrada_var1.get())  # se hace porque es mas sensillo modificar la variable que el componente
    # Modificacion ultilizamos la variable de texto (set)
    #entrada_var1.set('Cambio...')
    # Recuperamos la informacion de las dos formas
    print(entrada1.get())
    print(entrada_var1.get())
    #Modificamos el texto del label
    etiqueta1.config(text=entrada_var1.get())

# Creamos un boton
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

ventana.mainloop()