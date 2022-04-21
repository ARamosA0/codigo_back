import tkinter


from tkinter import *
from tkinter import messagebox

def saludar():
    print('Hola')
    messagebox.showinfo("mensaje", "hola" + txtNombre.get())

app = Tk()
app.title('Mi primera interfaz grafica')
app.geometry('450x450')
frame = LabelFrame(app, text='Mi ventana')
frame.grid(row=0, column=0, columnspan=3, pady=10)

#label
lbNombre = Label(app, text='Nombre: ')
lbNombre.grid(row=1, column=0)

#caja de texto
txtNombre = Entry(frame)
txtNombre.grid(row=1, column=1)

#boton
btnSaludo = Button(frame, text='salidar', command=saludar)
btnSaludo.grid(row=1, column=2)

app.mainloop()

