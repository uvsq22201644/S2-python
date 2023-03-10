import tkinter as tk
from random import randint
from numpy import sqrt
color=''

def couleur():
    global color 
    color=input('couleur : ')

def circle():
    predef='blue'
    if color !='':
        predef=color 
    coordx= randint(60,340)
    coordy=randint(60,340)
    canvas.create_oval(coordx-50,coordy-50,coordx+50,coordy+50, outline=predef)

def carre():
    predef='red'
    if color != '':
        predef=color
    coordx=randint(10,248)
    coordy= randint(10,248)
    canvas.create_rectangle(coordx,coordy,coordx+100,coordy+100,outline=predef)


def croix():
    predef='yellow'
    if color!= '':
        predef=color
    coordx=randint(10,248)
    coordy=randint(10,248)
    canvas.create_line(coordx,coordy,coordx+sqrt(2)*100,coordy+sqrt(2)*100,fill=predef)
    canvas.create_line(coordx+sqrt(2)*100,coordy,coordx,coordy+sqrt(2)*100,fill=predef)


window= tk.Tk()
window.title("Mon dessin")
CANVASWIDTH=400
CANVASHEIGHT=400

canvas=tk.Canvas(window,width=CANVASWIDTH,height=CANVASHEIGHT,bg="black",bd='10',relief='raised')

canvas.grid(row=1,rowspan=3,column=1)

boutoncolor=tk.Button(window,text="Choisir une couleur",underline='1',command=couleur)
boutoncolor.grid(column=1,row=0)
boutoncircle=tk.Button(window,text="Cercle",relief='sunken',command=circle)
boutoncircle.grid(column=0,row=1)
boutonsquare=tk.Button(window,text="Carré",font='write',fg='blue',command=carre)
boutonsquare.grid(column=0,row=2)
boutoncross=tk.Button(window,text="Croix",bg='yellow',bd='5',command=croix)
boutoncross.grid(column=0,row=3)

window.mainloop()