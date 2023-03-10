import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

if __name__=='__main__':
    root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x0 = 100
x1 = CANVAS_WIDTH - 100
x = CANVAS_WIDTH // 2
y0= 50
y1=CANVAS_HEIGHT-50
canvas.create_line(x, y0, x, y1)
canvas.create_oval(x - 50, y0+ 50, x + 50, y1 - 50)
canvas.create_oval(x - 50, y0 + 50, x + 50, y1 - 50)
canvas.create_oval((x + x) / 2 - 50, y0 + 50, (x + x) / 2 + 50, y1 - 50)

# Fin de votre code

canvas.grid()
root.mainloop()