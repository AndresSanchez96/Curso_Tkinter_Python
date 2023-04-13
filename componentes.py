import tkinter as tK
from tkinter import ttk, messagebox, scrolledtext
from time import sleep

ventana = tK.Tk()
ventana.geometry('600x400')
ventana.title('Componentes')
ventana.iconbitmap('icono.ico')

def crear_componentes_tabulador1(tabulador):
    # Agregar una etiqueta y un componente de entrada
    etiqueta1 = ttk.Label(tabulador, text='Nombre:')
    etiqueta1.grid(row=0, column=0, sticky=tK.E)
    entrada1 = ttk.Entry(tabulador, width=30)
    entrada1.grid(row=0, column=1, padx=5, pady=5)
    # Agregamos u boton
    def enviar():
        messagebox.showinfo('Mensaje', f'Nombre: {entrada1.get()}')

    boton1 = ttk.Button(tabulador, text='Enviar', command=enviar)
    boton1.grid(row=1, column=0, columnspan=2)

def crear_componentes_tabulador2(tabulador):
    contenido = 'Este es mi texto con el contenido'
    # Creamos el componente del scroll
    scroll = scrolledtext.ScrolledText(tabulador, width=50, height=10, wrap=tK.WORD)
    scroll.insert(tK.INSERT, contenido)
    # Mostramos el componente
    scroll.grid(row=0, column=0)


def crear_componentes_tabulador3(tabulador):
    # Creamos una lista usando data list comprehensions
    datos = [x+1 for x in range(10)]
    combobox = ttk.Combobox(tabulador, width=15, values=datos)
    combobox.grid(row=0, column=0, padx=10, pady=10)
    #Seleccionamos un elemento por default
    combobox.current(5)
    #agregamos un tboton para saber que opcion selecciono el usuario
    def mostrar_valor():
        messagebox.showinfo('Valor Seleccionado', f'Valor seleccionado {combobox.get()}')
    boton1 = ttk.Button(tabulador, text='Mostrar valor seleccionado', command=mostrar_valor)
    boton1.grid(row=0, column=1)

def crear_componentes_tabulador4(tabulador):
    imagen = tK.PhotoImage(file='python-logo.png')
    def mostrar_titulo():
        messagebox.showinfo('Mas info de la imagen', f'Nombre de la imagen: {imagen.cget("file")}')
    boton_imagen = ttk.Button(tabulador, image=imagen, command=mostrar_titulo)
    boton_imagen.grid(row=0, column=0)

def crear_componentes_tabulador5(tabulador):
    #Creamos el componenete de barra de progreso
    barra_progreso = ttk.Progressbar(tabulador, orient='horizontal', length=550)
    barra_progreso.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
    #Agregamos los botones para controlar los eventos de la barra
    def ejecutar_barra():
        barra_progreso['maximum'] = 100
        for valor in range(101):
            # Mandamos a espera un poco antes de continuar con la ejecucion de la barra
            sleep(0.05)
            #Incrementamos la barra de progreso
            barra_progreso['value'] = valor
            # Actualizamos la barra de progreso
            barra_progreso.update()
        barra_progreso['value'] = 0

    def ejecutar_ciclo():
        barra_progreso.start()

    def detener():
        barra_progreso.stop()

    def detener_despues():
        esperar_ms = 1000
        ventana.after(esperar_ms, barra_progreso.stop())

    boton_inicio = ttk.Button(tabulador, text='Ejecutar barra de progreso', command= ejecutar_barra)
    boton_inicio.grid(row=1, column=0)
    boton_ciclo = ttk.Button(tabulador, text='Ejecutar Ciclo', command=ejecutar_ciclo)
    boton_ciclo.grid(row=1, column=1)
    boton_detener = ttk.Button(tabulador, text='Detener ejecucion', command=detener)
    boton_detener.grid(row=1, column=2)
    boton_despues = ttk.Button(tabulador, text='Detener ejecucion despues', command=detener_despues)
    boton_despues.grid(row=1, column=3)

def crear_tabs():
    # Creamos un tab control, para ello usamos la clase de notebook
    control_tabulador = ttk.Notebook(ventana)

    # Agregamos un marco o frame para agegar dentro del tab y organizar
    tabulador1 = ttk.Frame(control_tabulador)
    # Agregamos el tabulador al control de tabuladores
    control_tabulador.add(tabulador1, text='Tabulador 1')
    # mostramos el tabulador
    control_tabulador.pack(fill='both')
    # Creamos un metodo para el tabulador 1
    crear_componentes_tabulador1(tabulador1)

    #Creamo un segundo tabulador para scrolled
    tabulador2 = ttk.Labelframe(control_tabulador, text='Contenido')
    control_tabulador.add(tabulador2, text='Tabulador 2')
    # Creamos los componentes del segundo tabulador
    crear_componentes_tabulador2(tabulador2)

    # Cremos un tercer tabulador para datalist
    tabulador3 = ttk.Labelframe(control_tabulador, text='Contenido')
    control_tabulador.add(tabulador3, text='Tabulador 3')
    #cramos los componenets del tercer tabulador
    crear_componentes_tabulador3(tabulador3)

    #Creamos un tabluador para imagenes
    tabulador4 = ttk.Labelframe(control_tabulador, text='Imagen')
    control_tabulador.add(tabulador4, text='Tabulador 4 ')
    #Creamos los componenetes del cuarto tabulador
    crear_componentes_tabulador4(tabulador4)

    #Creamos un nuevo tabulador para barra de progreso
    tabulador5 = ttk.Labelframe(control_tabulador, text='Barra de progreso')
    control_tabulador.add(tabulador5, text='Tabulador 5')
    #creamos los componenetes del quinto tabulador
    crear_componentes_tabulador5(tabulador5)

crear_tabs()
ventana.mainloop()