import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext


class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x480')
        self.resizable(0,0)
        self.title('Calculadora')
        self.iconbitmap('calculadora.ico')

        # Atributos de clase
        self.expresion = ''
        # Caja de texto
        self.entrada = None
        # StringVar lo utilizamos para actualizar el valor del input
        self.entrada_texto = tk.StringVar()
        # Creamos un metodo de componentes
        self._creacion_componentes()

    #Metodos de clase
    # Metodos para la creacion de componentes
    def _creacion_componentes(self):
        # Creamo un frame para la caja de texto
        entrada_frame = tk.Frame(self, width=400, height=50, bg='grey')
        entrada_frame.pack(side=tk.TOP) # se publica en la parte superior
        #caja de texto
        entrada = tk.Entry(entrada_frame, font=('arial', 18, 'bold'),
                           textvariable=self.entrada_texto, width=30,
                           justify=tk.RIGHT)
        entrada.grid(row=0, column=0, ipady=10)

        # Creamos un segundo frame para la parte inferior
        botones_frame = tk.Frame(self, width=400, height=450, bg='grey')
        botones_frame.pack()

        # Primer renglon
        boton_limpiar = tk.Button(botones_frame, text='C', width=41, height=5,
                                  bd=0, bg='#eee', cursor='hand2',
                                  command=self._evento_limpiar)
        boton_limpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

        boton_dividir = tk.Button(botones_frame, text='/', width=13, height=5,
                                  bd=0, bg='#eee', cursor='hand2',
                                  command=lambda: self._evento_click('/'))
        boton_dividir.grid(row=0, column=3, padx=1, pady=1)

        # Segundo renglon
        boton_siete = tk.Button(botones_frame, text='7', width=13, height=5,
                                bd=0, bg='#fff', cursor='hand2',
                                command= lambda: self._evento_click(7))
        boton_siete.grid(row=1, column=0, pady=1, padx=1)

        boton_ocho = tk.Button(botones_frame, text='8', width=13, height=5,
                                bd=0, bg='#fff', cursor='hand2',
                                command=lambda: self._evento_click(8))
        boton_ocho.grid(row=1, column=1, pady=1, padx=1)

        boton_nueve = tk.Button(botones_frame, text='9', width=13, height=5,
                                bd=0, bg='#fff', cursor='hand2',
                                command=lambda: self._evento_click(9))
        boton_nueve.grid(row=1, column=2, pady=1, padx=1)

        boton_multiplicar = tk.Button(botones_frame, text='*', width=13, height=5,
                                  bd=0, bg='#eee', cursor='hand2',
                                  command=lambda: self._evento_click('*'))
        boton_multiplicar.grid(row=1, column=3, padx=1, pady=1)

        # Tercer renglon
        boton_cuatro = tk.Button(botones_frame, text='4', width=13, height=5,
                                bd=0, bg='#fff', cursor='hand2',
                                command=lambda: self._evento_click(4))
        boton_cuatro.grid(row=2, column=0, pady=1, padx=1)

        boton_cinco = tk.Button(botones_frame, text='5', width=13, height=5,
                               bd=0, bg='#fff', cursor='hand2',
                               command=lambda: self._evento_click(5))
        boton_cinco.grid(row=2, column=1, pady=1, padx=1)

        boton_seis = tk.Button(botones_frame, text='6', width=13, height=5,
                                bd=0, bg='#fff', cursor='hand2',
                                command=lambda: self._evento_click(6))
        boton_seis.grid(row=2, column=2, pady=1, padx=1)

        boton_restar = tk.Button(botones_frame, text='-', width=13, height=5,
                                      bd=0, bg='#eee', cursor='hand2',
                                      command=lambda: self._evento_click('-'))
        boton_restar.grid(row=2, column=3, padx=1, pady=1)

        # Cuarto renglon
        boton_uno = tk.Button(botones_frame, text='1', width=13, height=5,
                                bd=0, bg='#fff', cursor='hand2',
                                command=lambda: self._evento_click(1))
        boton_uno.grid(row=3, column=0, pady=1, padx=1)

        boton_dos = tk.Button(botones_frame, text='2', width=13, height=5,
                               bd=0, bg='#fff', cursor='hand2',
                               command=lambda: self._evento_click(2))
        boton_dos.grid(row=3, column=1, pady=1, padx=1)

        boton_tres = tk.Button(botones_frame, text='3', width=13, height=5,
                                bd=0, bg='#fff', cursor='hand2',
                                command=lambda: self._evento_click(3))
        boton_tres.grid(row=3, column=2, pady=1, padx=1)

        boton_sumar = tk.Button(botones_frame, text='+', width=13, height=5,
                                      bd=0, bg='#eee', cursor='hand2',
                                      command=lambda: self._evento_click('+'))
        boton_sumar.grid(row=3, column=3, padx=1, pady=1)

        # Quinto renglon
        boton_cero = tk.Button(botones_frame, text='0', width=27, height=5,
                               bd=0, bg='#fff', cursor='hand2',
                               command= lambda: self._evento_click(0))
        boton_cero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

        boton_punto = tk.Button(botones_frame, text='.', width=13, height=5,
                                bd=0, bg='#eee', cursor='hand2',
                                command=lambda: self._evento_click('.'))
        boton_punto.grid(row=4, column=2, padx=1, pady=1)

        boton_igual = tk.Button(botones_frame, text='=', width=13, height=5,
                                bd=0, bg='#eee', cursor='hand2',
                                command=self._evento_evaluar)
        boton_igual.grid(row=4, column=3, padx=1, pady=1)

    def _evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion) # set modifica valores

    def _evento_click(self, elemento):
        # Concatenamos el nuevo elemento que se presiono
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)

    def _evento_evaluar(self):
        # eval evalua la expresion de tipo str como una expresion aritmetica
        try:
            if self.expresion:
                resultado = str(eval(self.expresion))
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrio un error: {e}')
            self.entrada_texto.set('')
        self.expresion = ''

if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()