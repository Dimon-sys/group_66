from tkinter import *
import random

#Окно
window = Tk()

w = 600
h = 600

window.geometry(str(w) + 'x' + str(h))

#Холст
canvas = Canvas(window, width = w, height = h)
canvas.place(in_ = window, x = 0, y = 0)

#Фон для игры 
bg_photo = PhotoImage(file = 'bg_2.png')

#Класс рыцарь
class Knight:
    def __init__(self):
        #Координаты рыцаря
        self.x = 70
        self.y = h // 2
        #Скорости рыцаря
        self.v_y = 0
        self.v_x = 0
        #Изображение
        self.photo = PhotoImage(file = 'knight.png')

    #Остановка
    def stop(self, event):
        self.v_y = 0
        self.v_x = 0

    #Движение вверх
    def up(self, event):
        if self.y - 2 <= 0:
            self.v_y = 0
        else:
            self.v_y = -3

    #Движение вниз
    def down(self, event):
        if self.y + 2 >= 600:
            self.v_y = 0
        else:
            self.v_y = 3

    def right(self, event):
        if self.x - 2 >= 600:
            self.v_x = 0
        else:
            self.v_x = 3 

    def left(self, event):
        if self.x - 2 <= 0:
            self.v_x = 0
        else:
            self.v_x = -3 


#Класс Дракон
class Dragon:
    def __init__(self):
        self.x = 750
        self.y = random.randint(100,500)
        self.v = random.randint(1,3)
        self.photo = PhotoImage(file = 'dragon.png')


knight = Knight()

dragons = []
for i in range(3):
    dragons.append(Dragon())


def game():
    canvas.delete('all')
    canvas.create_image(300,300, image = bg_photo)
    canvas.create_image(knight.x, knight.y, image = knight.photo)
    knight.y += knight.v_y 
    knight.x += knight.v_x


    current_dragon = 0
    dragon_to_kill = -1

    for dragon in dragons:
        dragon.x -= dragon.v
        canvas.create_image(dragon.x, dragon.y, image = dragon.photo)

        if ((dragon.x - knight.x) ** 2) + ((dragon.y - knight.y) ** 2) <= (96) ** 2:
            dragon_to_kill = current_dragon

        current_dragon += 1

        if dragon.x <= 0:
            canvas.delete('all')
            canvas.create_text(w//2, h//2, text = 'You lose!', font = 'Verdana 42', fill = 'red')
            break


    if dragon_to_kill >= 0:
        del dragons[dragon_to_kill] 

    if len(dragons) == 0:
        canvas.delete('all')
        canvas.create_text(w//2, h//2, text = 'You win!', font = 'Verdana 42', fill = 'red')
    else:
        window.after(5, game)


game()

window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<KeyRelease>', knight.stop)
window.bind('<Key-Right>', knight.right)
window.bind('<Key-Left>', knight.left)


window.mainloop()
