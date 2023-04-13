import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de grid')
ventana.iconbitmap('icono.ico')

#width es la cantidad de caracteres que ocupa la caja de texto
# se define una variable que se podra modificar posteriormente (set), leer(get)
entrada_var1 = tk.StringVar(value='Valor por default')
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada_var1)

#entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER)
entrada1.grid(row=0, column=0)

# insert agrega un texto a la caja de texto
#entrada1.insert(0, 'Nombre')
entrada1.insert(tk.END, '.')
#entrada1.config(show='*')
#entrada1.config(state='readonly')

def enviar():
    #print(entrada1.get())
    #boton1.config(text=entrada1.get())
    # Eliminar contenido
    #entrada1.delete(0, tk.END)
    #Seleccionar el texto de la cja
    #entrada1.select_range(0, tk.END)
    #para hacer efectivo la seleccion del texto
    #entrada1.focus()

    #recuperamos la informacion a partir de la variable asociada con la caja de texto
    boton1.config(text=entrada_var1.get()) # se hace porque es mas sensillo modificar la variable que el componente
    #Modificacion ultilizamos la variable de texto (set)
    entrada_var1.set('Cambio...')
    # Recuperamos la informacion de las dos formas
    print(entrada1.get())
    print(entrada_var1.get())


# Creamos un boton
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

ventana.mainloop()
