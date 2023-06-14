from tkinter import *

window = Tk()
width_w = window.winfo_screenwidth()
height_w = window.winfo_screenheight()
window.geometry(str(width_w) + 'x' + str(height_w))

w =700
h = 700
canvas = Canvas(window, width=w, height=h)
canvas.place(in_= window, x = 0, y = 0)

class Painting:
    def __init__(self, square_x_1, square_y_1, square_x_2, square_y_2, triangle_x1, triangle_y1, triangle_x2, triangle_y2, triangle_x3, triangle_y3):
        self.square_x_1 = square_x_1
        self.square_y_1 = square_y_1
        self.square_x_2 = square_x_2
        self.square_y_2 = square_y_2
        self.triangle_x1 = triangle_x1
        self.triangle_y1 = triangle_y1
        self.triangle_x2 = triangle_x2
        self.triangle_y2 = triangle_y2
        self.triangle_x3 = triangle_x3
        self.triangle_y3 = triangle_y3
    def build(self, square_x_1, square_y_1, square_x_2, square_y_2, triangle_x1, triangle_y1, triangle_x2, triangle_y2, triangle_x3, triangle_y3):
        self.square_x_1 = square_x_1
        self.square_y_1 = square_y_1
        self.square_x_2 = square_x_2
        self.square_y_2 = square_y_2
        self.triangle_x1 = triangle_x1
        self.triangle_y1 = triangle_y1
        self.triangle_x2 = triangle_x2
        self.triangle_y2 = triangle_y2
        self.triangle_x3 = triangle_x3
        self.triangle_y3 = triangle_y3
        self.square = canvas.create_rectangle(square_x_1, square_y_1, square_x_2, square_y_2, fill='yellow', outline='black')
        self.triangle = canvas.create_polygon(triangle_x1, triangle_y1, triangle_x2, triangle_y2, triangle_x3, triangle_y3, fill='red', outline='green')
    


figures = Painting(30, 30, 50, 50, 100, 10, 150, 300, 80, 80)
figures.build(30, 30, 50, 50, 100, 10, 150, 300, 80, 80)


window.mainloop()