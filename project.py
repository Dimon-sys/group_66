from tkinter import *

window = Tk()
width_w = window.winfo_screenwidth()
height_w = window.winfo_screenheight()
window.geometry(str(width_w) + 'x' + str(height_w))

main_hero = PhotoImage(file="main_hero.png", width=50, height=70, x=200, y=200)
y_hero = 200
x_hero = 200
def forward():
    global x_hero, y_hero, main_hero
    y_hero += 1
    main_hero.configure(y=y_hero)
def back():
    global x_hero, y_hero, main_hero
    y_hero -= 1
    main_hero.configure(y=y_hero)
def left():
    global x_hero, y_hero, main_hero
    x_hero -= 1
    main_hero.configure(x=x_hero)
def right():
    global x_hero, y_hero, main_hero
    x_hero += 1
    main_hero.configure(x=x_hero)

def game_started():
    global label
    fow = Button(text="//\\", fg='black', bg='white', font=('Courier New', 34), command=forward)
    fow.place(x=20, y=20, width=100, height=100)
    bac = Button(text="\\//", fg='black', bg='white', font=('Courier New', 34), command=back)
    bac.place(x=20, y=10, width=100, height=100)
    lef = Button(text="<<", fg='black', bg='white', font=('Courier New', 34), command=left)
    lef.place(x=10, y=10, width=100, height=100)
    righ = Button(text=">>", fg='black', bg='white', font=('Courier New', 34), command=right)
    righ.place(x=300, y=10, width=100, height=100)
    label.destroy


label = Label(text=' ______   _______   ______   _________   _____   ______\n  |   ___| |  _____| |   ___| |   ____  | |  _  | |   ___|\n  |  |___  |  |____  |  |     |  |____| | | |_| | |  |___ \n   |   ___| |_____  | |  |     |   ____  | | ____| |   ___| \n  |  |___   ____|  | |  |___  |  |    | | | |     |  |___ \n  |______| |_______| |______| |__|    |_| |_|     |______|', fg='black', bg='white', font=('Courier New', 34))
label.place(x=0, y=100, width=1500, height=200)

b_1 = Button(text='Начать игру', fg='red', bg='white', font=('Courier New', 34), command=game_started)
b_1.place(x=70, y=380, width=1200, height=50)

window.mainloop()
