from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("Product management")
raiz.config(bg='brown')
raiz.geometry("600x450")

mainFrame = Frame(raiz, bg="brown")
mainFrame.grid(column= 0, row=0)
secondFrame = Frame(mainFrame, bg='brown')
secondFrame.grid(column=2, row=2)
thirdFrame = Frame(mainFrame, bg='brown')
thirdFrame.grid(column=3, row=2)
Label(mainFrame, bg="brown", text="   ").grid(column=1, row=1)

#secondFrame
Label(secondFrame, bg='brown', text= "Id product:").grid(column=1, row=1, sticky=(E))
Label(secondFrame, bg='brown', text= "").grid(column=1, row=2)
Label(secondFrame, bg='brown', text= "Name:").grid(column=1, row=3, sticky=(E))
Label(secondFrame, bg='brown', text= "").grid(column=1, row=4)
Label(secondFrame, bg='brown', text= "Description:").grid(column=1, row=5, sticky=(E))
Label(secondFrame, bg='brown', text= "").grid(column=1, row=6)
Label(secondFrame, bg='brown', text= "Quantity:").grid(column=1, row=7, sticky=(E))
Label(secondFrame, bg='brown', text= "").grid(column=1, row=8)
Label(secondFrame, bg='brown', text= "Price:").grid(column=1, row=9, sticky=(E))
Label(secondFrame, bg='brown', text= "    ").grid(column=2, row=1)

idEntry = Entry(secondFrame, bg='brown', width = 30)
idEntry.grid(column=3, row=1)
nameEntry = Entry(secondFrame, bg='brown', width = 30)
nameEntry.grid(column=3, row=3)
descriptionEntry = Entry(secondFrame, bg='brown', width = 30)
descriptionEntry.grid(column=3, row=5)
quantityEntry = Entry(secondFrame, bg='brown', width = 30)
quantityEntry.grid(column=3, row=7)
priceEntry = Entry(secondFrame, bg='brown', width = 30)
priceEntry.grid(column=3, row=9)

#thirdFrame
imagen4 = PhotoImage(file= "BackBotton.png")
btnImagen = Button(thirdFrame, bg='brown')
btnImagen.grid(column=1, row=1)
btnImagen['image'] = imagen4

Label(thirdFrame, bg="brown", text="").grid(column=1, row=2)

imagen1 = PhotoImage(file= "SaveBotton.png")
btnImagen = Button(thirdFrame, bg='brown')
btnImagen.grid(column=1, row=3)
btnImagen['image'] = imagen1

imagen2 = PhotoImage(file= "DeleteBotton.png")
btnImagen = Button(thirdFrame, bg='brown')
btnImagen.grid(column=1, row=4)
btnImagen['image'] = imagen2

imagen3 = PhotoImage(file= "UpdateBotton.png")
btnImagen = Button(thirdFrame, bg='brown')
btnImagen.grid(column=1, row=5)
btnImagen['image'] = imagen3

#Imagen de tabla
Label(mainFrame, bg="brown", text="   ").grid(column=1, row=1)
Label(mainFrame, bg="brown", text="   ").grid(column=2, row=3)

imagen5 = PhotoImage(file= "Tabla.png")
etqImagen = Label(mainFrame, bg='brown')
etqImagen.grid(column=2, row=4, columnspan=3, sticky=(N, S, W, E))
etqImagen['image'] = imagen5

raiz.mainloop()