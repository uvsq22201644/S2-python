import tkinter as tk
from random import randint


def get_color(r,g,b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i,j,color):
    canvas.create_rectangle(i,j,i,j,fill=color,width=0)

def ecran_aleatoire():
    for i in range(0,255):
        for j in range (0,255):
            r,g,b=randint(0,255),randint(0,255),randint(0,255)
            draw_pixel(i,j,get_color(r,g,b))

def degrade_gris():
    color=0
    for i in range(257):
        for j in range(257):
            draw_pixel(i,j,get_color(color,color,color))
        color+=1

def degrade_2d():
    for i in range(255):
        for j in range(255):
            draw_pixel(i,j,get_color(i,0,j))

racine=tk.Tk()
racine.title("tk")

canvas= tk.Canvas(racine,width=256,height=256,bd=10,background="black")
boutonRandom=tk.Button(racine,test='Aléatoire',command=ecran_aleatoire)
boutonRandom.grid(row=0,column=0)
boutonDegGris=tk.Button(racine,text="Dégradé gris",command=degrade_gris)
boutonDegGris.grid(row=1,column=0)
boutonDeg2D=tk.Button(racine,text='Dégradé 2D',command=degrade_2d)
boutonDeg2D.grid(row=2,column=0)
canvas.grid(row=0,rowspan=3,column=1)
racine.mainloop()