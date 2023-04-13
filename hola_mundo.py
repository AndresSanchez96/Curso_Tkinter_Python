# GUI = Graphical User Interface
# Tkinter - TK Interface
# Importamos el modulo de tkinter
import tkinter as tk
# Importamos el modulo del tema de tkinter
from tkinter import ttk

#Creamos un objeto usando la clase tk
ventana = tk.Tk()
#Modificamos el tamaño de la ventana ( pixeles)
ventana.geometry('600x400')
#cambiamos el nombre de la ventana
ventana.title('Hola mundo')
#Configuraoms el icono de la app
ventana.iconbitmap('icono.ico')

# Creamos un metodo evento_click
def evento_click():
    boton1.config(text='Boton presionado')
    print('Ejecucion del evento click')
    # Creamos un  uevo boton
    boton2 = ttk.Button(ventana, text='Nuevo boton')
    boton2.pack()

# Cramos un boton tambien conocido como componente o widget, el objeto padre es ventana
boton1 = ttk.Button(ventana, text='Dar click', command=evento_click)
# Utilizar el pack layout manager para mostrar el boton de la ventana
boton1.pack()
#Iniciar nuestra ventana (esta linea la ejecutamos al final)
#Si la ejecutamos antes no se muestran los cambios
ventana.mainloop()