from tkinter import *

window = Tk()
width_w = window.winfo_screenwidth()
height_w = window.winfo_screenheight()
window.geometry(str(width_w) + 'x' + str(height_w))

count_quest = 0

def score_plus():
    global count_quest
    count_quest += 1

def changes():
    global label, count_quest
    score_plus()
    if count_quest == 1:
        label.configure(text='Может ли страус назвать себя птицей?')
        b_1.configure(text='Да', command=NO)
        b_2.configure(text='Нет', command=changes)
        b_3.configure(text='Не знаю, надо у него спросить', command=NO)
    elif count_quest == 2:
        label.configure(text='На столе лежат два яблока и помидор.\n Сколько фруктов на полу?')
        b_1.configure(text='2', command=NO)
        b_2.configure(text='3', command=NO)
        b_3.configure(text='0', command=changes)
    elif count_quest == 3:
        label.configure(text='Два шахматиста играют 2 часа. \n Сколько часов играет каждый?')
        b_1.configure(text='2', command=changes)
        b_2.configure(text='4', command=NO)
        b_3.configure(text='3', command=NO)
    elif count_quest == 4:
        label.configure(text='КОНЕЦ ИГРЫ')
        b_1.configure(text='СПАСИБО', command=NO)
        b_2.configure(text='ЗА', command=NO)
        b_3.configure(text='ИГРУ', command=NO)

label = Label(text='Тест на внимательность', fg='black', bg='white', font=('Courier New', 34))
label.place(x=0, y=100, width=1500, height=200)

b_1 = Button(text='Чтобы начать нажмите на красную надпись', fg='red', bg='white', font=('Courier New', 34), command=changes)
b_1.place(x=50, y=380, width=1200, height=50)

b_2 = Button(text='Начать', fg='green', bg='white', font=('Courier New', 34))
b_2.place(x=50, y=430, width=1200, height=50)

b_3 = Button(text='Начать', fg='blue', bg='white', font=('Courier New', 34))
b_3.place(x=50, y=480, width=1200, height=50)




window.mainloop()