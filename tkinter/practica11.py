from tkinter import Tk,Frame,Button, messagebox

# 4. Funcion de mensajes
def mostrarMensaje():
    messagebox.showinfo("Aviso","Este mensaje es para avisar algo.")
    messagebox.showerror("Error:", "Todo fallo con exito.")
    print(messagebox.askokcancel("Pregunta:", "El o ella jugó con tu corazón."))
    print(messagebox.askquestion("Pregunta:", "El o ella jugó con tu corazón."))
    print(messagebox.askretrycancel("Pregunta:", "El o ella jugó con tu corazón."))
    print(messagebox.askyesno("Pregunta:", "El o ella jugó con tu corazón."))
    print(messagebox.askyesnocancel("Pregunta:", "El o ella jugó con tu corazón."))

#5. Funcion para crear botones

def agregarBoton():
    botonVerde.config(text="+", bg="green", fg="white")
    botonNuevo = Button(seccion3, text="Boton Nuevo")
    botonNuevo.pack()

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

botonAzul = Button(seccion1, text="Boton Azul", fg="blue", command=mostrarMensaje)
botonAzul.place(x=60, y=60)

botonAmarillo = Button(seccion2, text="Boton Amarillo", bg='yellow', fg='black', command=mostrarMensaje)
botonAmarillo.grid(row=0, column=0)

botonNegro = Button(seccion2, text="Boton Negro", bg='black', fg="white", command=mostrarMensaje)
botonNegro.grid(row=1, column=1)

botonVerde = Button(seccion3, text="Boton Verde",bg='#588c7e', fg="white", command=agregarBoton)
botonVerde.pack()

#Main de ejecucion de la ventana
ventana.mainloop()

#Prueba de git terminal