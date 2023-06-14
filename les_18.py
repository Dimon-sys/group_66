from tkinter import *

root = Tk()
root.title('Моё приложение')
root.geometry('500x500+200+200')

count=0
def changeLabel():
    global count
    count += 1
    lab['text'] = count


lab = Label(root, text='Текст', bg='#FF5463', fg='gold', font='16')
lab.place(x=100, y=100)


btn = Button(text='Кнопка', background='#555', foreground='#ccc', font='16', command=changeLabel)
btn.place(x=200, y=200)

root.mainloop()