import tkinter as tk
from tkinter import *
import requests
Succes=False
def end():
    global Succes
    if Succes:
        root.destroy()

root=tk.Tk()
root.title("Clima App")
root.geometry("400x200")

#etiqueta para pedir el nombre de la ciudad
label=Label(root,text="Ciudad")
label.grid(row=0,column=0)

#Entry para ingresar nombre de la ciudad
entry=Entry(root)
entry.grid(row=0,column=1)

#Boton de Búsqueda
buscar=Button(root,text="Buscar clima",command=lambda:fetcherpost(entry.get()))
buscar.grid(columnspan=2)

#Etiqueta para mostrar el resultado preliminar
lblPreliminar=Label(root,text="Resultado Preliminar")
lblPreliminar.grid(columnspan=2)

#etiqueta para mostrar el resultado final
lblResult=Label(root,text="Resultado")
lblResult.grid(columnspan=2)

#funcion para obtener el clima de la ciudad ingresada
def fetcherpost(city):
    global Succes
    lblPreliminar.configure(text="Obteniendo el clima de "+city+"...")
    api_key="8fa8765cc3f583722f90718bac1d3f36"
    #url del api en openweathermap
    url="http://api.openweathermap.org/data/2.5/weather"
    #parametros enviados al api
    params={"APPID":api_key, "q":city, "units":"metric"}
    #respuesta del api
    response=requests.get(url,params=params)
    if (response):
        Succes=True
        weather=response.json()
        clima=weather['weather'][0]['main']
        temperatura=weather['main']['temp']
        viento=weather['wind']['speed']
        summary='Clima : '+str(clima)+'\nTemperatura : '+str(temperatura)+'\nViento : '+str(viento)+" m/s"
        lblResult.configure(text=summary)
    else:
        lblResult.configure(text="No se puede obtener el clima de "+city)

root.protocol("WM_DELETE_WINDOW", end)
root.mainloop()