import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

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
    if mensaje1:
        messagebox.showinfo('Mensaje informativo', mensaje1 + ' Informativo')

def  salir():
    ventana.quit()
    ventana.destroy()
    sys.exit()

def crear_menu():
    # Configurar el menu principal
    menu_principal = Menu(ventana)
    #tearoff = False con el objetivo de que no se separe el menu de la interfaz
    menu_archivo = Menu(menu_principal, tearoff=False)
    # Agregamo una nueva opcion al menu de archivo
    menu_archivo.add_command(label='Nuevo')
    # AGregar un separador
    menu_archivo.add_separator()
    #Agregamos otra opcion de salir
    menu_archivo.add_command(label='Salir', command=salir)
    # Agregamos el submenu al munu principal
    menu_principal.add_cascade(menu=menu_archivo, label='Archivo')
    # Sub menu de ayuda
    menu_ayuda = Menu(menu_principal, tearoff=False)
    menu_ayuda.add_command(label='Acerda de...')
    menu_principal.add_cascade(menu=menu_ayuda, label='Ayuda')
    #MOstramos el munu en la ventana principal
    ventana.config(menu=menu_principal)

# Creamos un boton
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

crear_menu()
ventana.mainloop()