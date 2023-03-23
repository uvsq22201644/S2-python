from tkinter import *

WIDTH = 500
HEIGHT = 500
CERCLES = 50
BG_COLOR = '#000000'

if WIDTH <= HEIGHT :
    SIZE = WIDTH/(CERCLES*2)
else:
    SIZE = HEIGHT/(CERCLES*2)

couleurs =['blue','green','black','yellow','magenta','red']

root =Tk()

canvas = Canvas(root,width=WIDTH,height=HEIGHT,bg=BG_COLOR)
canvas.pack()

for i in range(CERCLES):
    canvas.create_oval(SIZE*i,SIZE*i,WIDTH-SIZE*i,HEIGHT-SIZE*i,fill=couleurs[i%len(couleurs)],width=0)

root.resizable(False,False)
root.mainloop()