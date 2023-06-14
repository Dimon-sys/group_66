from tkinter import *

def loh():
    text.configure(text='Чтобы забрать выйгрыш необходимо внести 1000руб.')

window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(str(width) + 'x' + str(height))

text = Label(text='ВЫ ВЫЙГРАЛИ В ЛОТЕРЕЕ!', fg='black', bg='white', font=('Courier New', 34))
text.place(x=100, y=200, width=1500, height=100)
b = Button(text='ПОЛУЧИТЬ ВЫЙГРЫШ!', fg='red', bg='white', command=loh)
b.place(x=750, y=500)

def on_close():
    loh()

window.protocol('WM_DELETE_WINDOW', on_close)

window.mainloop()