from tkinter import *

def check():
    global cur_q, points
    answer = var.get()
    if bool(answer) == facts[cur_q]['right']:
        points += 1
    if cur_q < len(facts) - 1:
        cur_q += 1
        fact['text'] = facts[cur_q]['text'] 
    else:
        points_label = Label(text='Вы набрали' + str(points) + 'очка', font=('Arial', 34), fg = 'red', bg = 'white')
        points_label.place(x=0, y=0, width=700, height=250)
        if points > len(facts) / 2:
            label_happy.place(x=0, y=250, width=700, height=250)
        else:
            label_sad.place(x=0, y=250, width=700, height=250)

window = Tk()
window.geometry('700x500')
window.title('Тест по вселенной "Доктор Кто"')

facts = [
{'text': 'Дэвид Тэннант сыграл 11-го Доктора', 'right': 1},
{'text': 'Хер - культовый антагонист Доктора', 'right': 0},
{'text': 'Перезапуск Доктора Кто состоялся в 2005', 'right': 1},
{'text': 'Нет', 'right': 0},
]

cur_q = 0
points = 0

label_tatle = Label('Тестирование по вселенной Доктор Кто', font = ('Arial', 24), fg = 'white', bg = 'red')
label_tatle.place(width=700, height=50, x=0, y=0)

fact = Message(text=facts[cur_q]['text'], font=('Arial', 14), width=680, borderwidth=0)
fact.config(justify=CENTER)
fact.place(x=10, y=70)

var = IntVar()
true = Radiobutton(text='Правда', variable=var, value=1)
true.place(x=10, y=120)

false = Radiobutton(text='Ложь', variable=var, value=0)
false.place(x=10, y=170)

b = Button(text='Ответить', font=('Arial', 24), fg = 'black', command=check)
b.place(x=200, y=130)

pic_happy = PhotoImage(file='happy.png')
label_happy = Label(image=pic_happy)

pic_sad = PhotoImage(file='sad.png')
label_sad = Label(image=pic_sad)

window.mainloop()