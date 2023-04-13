import tkinter as tk
from tkinter import ttk, messagebox, Menu

class Login(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x130')
        self.title('Login')
        self.iconbitmap('icono.ico')
        self.resizable(0,0) # se bloquea la ventana para que no cambie el tamaño

        # Configuramos el grid

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self._crear_componentes()

    #Definir el metodo crear_componentes
    def _crear_componentes(self):
        # Usuario
        etiqueta1 = tk.Label(self, text='Usuario: ')
        etiqueta1.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.entrada1 = ttk.Entry(self, width=30)
        self.entrada1.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        #Password
        etiqueta2 = tk.Label(self, text='Password: ')
        etiqueta2.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.entrada2 = ttk.Entry(self, width=30)
        self.entrada2.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        self.entrada2.config(show='*')

        # Defninimos dos botones
        boton1 = ttk.Button(self, text='Login', command=self._login)
        boton1.grid(row=3, column=0, columnspan=2)

    def _login(self):
        messagebox.showinfo('Datos Login', f'Usuario: {self.entrada1.get()}, Password: {self.entrada2.get()}')


if __name__ == '__main__':
    login_ventana = Login()
    login_ventana.mainloop()