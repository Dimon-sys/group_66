from tkinter import *
#life_sim
def count_start():
    if int(count_text['text']) > 0:
        count_text['text'] = int(count_text['text']) - 1
        count_text.place(x=250, y=25, width=400, height=100)
        window.after(1000, count_start)
    else:
        count_text['text'] = 0
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        window.geometry(str(width) + 'x' + str(height))
        photo = PhotoImage(file='skelet.gif')
        label = Label(image=photo, bg= 'black')
        label.image = photo
        label.place(width=width, height=height, x=0, y=0)

def on_close():
    count_start()

window = Tk()
window.geometry('900x300')
window.title('Вирус')
window.resizable(width=False, height=False)
window.config(bg='black')

text = Label(text='Ваш компьютер заражён!!!!!', fg='green', bg='black', font=('Courier New', 34))
text.place(x=100, y=100, width=700, height=100)
count_text = Label(text='6', fg='green', bg='black', font=('Courier New', 38))

window.protocol('WM_DELETE_WINDOW', on_close)

window.mainloop()

