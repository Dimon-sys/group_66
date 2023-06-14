from tkinter import *

window = Tk()
window.geometry('700x600')

def draw_home_button():
    b =Button(text= 'Домой', font=('Arial', 24), fg='black', command=draw_menu)
    b.place(x=25, y=500, width=150)

def clear():
    all_widgets = window.place_slaves()
    for i in all_widgets:
        i.destroy()
    draw_home_button()

def draw_menu():
    clear()
    label_title = Label(text='Что бы вы хотели сделать?', font= ('Arial', 24), fg='white', bg='orange')
    label_title.place(width=700, height=50, x=0, y=0)
    b_1 = Button(text='Узнать что-то новое', font=('Arial, 18'), fg='black', command=clear)
    b_1.place(x=25, y=75, width=300)

    b_2 = Button(text='Посмотреть фото', font=('Arial', 18), fg='black', command=clear)
    b_2.place(x=375, y=75, width=300)

draw_menu()

window.mainloop()