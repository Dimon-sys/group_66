import random
from tkinter import *

window = Tk()
window.title("Алхимия")
window.geometry("600x600")

class Fire:
    image = PhotoImage(file="fire.png").subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Earth):
            return Clay
        if isinstance(other, Water):
            return Steam
        

class Water:
    image = PhotoImage(file="water.png").subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam

class Wind:
    image = PhotoImage(file="wind.png").subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Earth):
            return Dust

class Steam:
    image = PhotoImage(file = 'aroma.png').subsample(4, 4)

class Dust:
    image = PhotoImage(file = 'dust.png').subsample(4,4)

class Earth:
    image = PhotoImage(file="ground.png").subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Fire):
            return Clay
        if isinstance(other, Wind):
            return Dust

class Clay:
    image = PhotoImage(file="pottery.png").subsample(4, 4)
    def __add__(self, other):
        pass

canvas = Canvas(window, width=600, height=600)
canvas.pack()
elements = [Earth(), Fire(), Water(), Wind()]

for element in elements:
    canvas.create_image(random.randint(50, 550), random.randint(50, 550), image=element.image)

def move(event):
    print(event)
    images_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    print(images_id)
    if len(images_id) == 2:
        element_id_1, element_id_2 = images_id[0], images_id[1]
        element_1 = elements[element_id_1 - 1]
        element_2 = elements[element_id_2 - 1]
        new_element = element_1 + element_2
        if new_element is not None and new_element not in elements:
            canvas.create_image(event.x, event.y, image=new_element.image)
            elements.append(new_element)
    canvas.coords(images_id, event.x, event.y)


window.bind("<B1-Motion>", move)

window.mainloop()






#
#         new_element = element_1 + element_2
#         if new_element not in elements:
#             canvas.create_image(event.x, event.y, image=new_element.image)
#             elements.append(new_element)
#
#     canvas.coords(images_id, event.x, event.y)
#
# window.mainloop()




















