from tkinter import *
import time 
import random
import emoji

def check_1():
    global points, points_1, points_2
    b_1.place(x=random.randint(1, 550), y=random.randint(1, 350))
    points += 1
    label['text'] = points
    points_1 += 1
    if points_2 - points_1 > 10:
        b_1.configure(text=emoji.emojize('Ну пожалуйста ::'))
    if points_1 == 20:
        b_1.configure(bg = 'red')
        time.sleep(2)
def check_2():
    global points, points_1, points_2
    b_2.place(x=random.randint(1, 550), y=random.randint(1, 350))
    points += 1
    label['text'] = points
    points_2 += 1
    if points_1 - points_2 > 10:
        b_2.configure(text=emoji.emojize('Ну пожалуйста ::'))
    if points_2 == 20:
        b_2.configure(bg = 'red')
        time.sleep(2)


window = Tk()
window.geometry('700x500')
window.title('Кликер')

points = 0
points_1 = 0
points_2 = 0

b_1 = Button(text='нажми на меня', font=('Arial', 29), fg = 'black', command=check_1)
b_1.place(x=200, y=130)

b_2 = Button(text='нажми на меня', font=('Arial', 29), fg = 'black', command=check_2)
b_2.place(x=300, y=130)


label = Label(text=points, font=('Arial', 15), fg = 'black')
label.place(x=10, y=10)

window.mainloop()