from tkinter import Tk,Frame,Button

#1. Crear ventana.

ventana = Tk() #Crear un objeto apartir de una clase es INSTANCIAR
ventana.title("Practica 11: Frames")
ventana.geometry("600x400")

#2. Definimos las secciones de la ventana.
seccion1 = Frame(ventana, bg='#80ced6')
seccion1.pack(expand=True, fill= 'both')

seccion2 = Frame(ventana, bg='#618685')
seccion2.pack(expand=True, fill='both')

seccion3 = Frame(ventana, bg='#ffef96')
seccion3.pack(expand=True, fill="both")

#3. Botones

botonAzul = Button(seccion1, text="Boton Azul", fg="blue")
botonAzul.place(x=60, y=60)

botonAmarillo = Button(seccion2, text="Boton Amarillo", bg='yellow', fg='black')
botonAmarillo.grid(row=0, column=0)

botonNegro = Button(seccion2, text="Boton Negro", bg='black', fg="white")
botonNegro.grid(row=1, column=1)

botonVerde = Button(seccion3, text="Boton Verde",bg='#588c7e', fg="white" )
botonVerde.pack()

#Main de ejecucion de la ventana
ventana.mainloop()