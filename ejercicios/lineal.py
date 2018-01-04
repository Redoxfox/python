#!/usr/lib/python3.6/tkinter/
from tkinter import *
ventana = Tk()
ventana.title('Algebra lineal')
ventana.geometry('400x400')
ventana.Entry = []
for i in range (3):
   for x in range(3):	
   		ventana.Entry.append(Entry(ventana, textvariable='0'))
   		ventana.Entry[x].place(x=60*i, y=40*x, width=100, height=30)

"""canvas = Canvas(width=300, height=210, bg='white')
canvas.pack(expand=YES, fill=BOTH)
canvas.create_line(0, 200, 200, 0, width=10, fill='green')
canvas.create_line(0, 0, 200, 0, width=10, fill='red')"""


# Code to add widgets will go here...
ventana.mainloop()
