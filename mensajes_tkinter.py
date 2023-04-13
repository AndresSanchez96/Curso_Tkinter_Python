import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de grid')
ventana.iconbitmap('icono.ico')

entrada1 = ttk.Entry(ventana, width=30)
entrada1.grid(row=0, column=0)

#Etiqueta o Label
etiqueta1 = tk.Label(ventana, text='Aqui se mostrara el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)

def enviar():

    #Modificamos el texto del label
    etiqueta1.config(text=entrada1.get())
    #Messagebox (cajas mensajes)
    mensaje1 = entrada1.get()
    #messagebox.showinfo('Mensaje informativo', mensaje1 + ' Informativo')
    #messagebox.showerror('Mensaje de Errror', mensaje1 + ' Error')
    messagebox.showwarning('Mensaje de alerta', mensaje1 + ' Alerta')

# Creamos un boton
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

ventana.mainloop()