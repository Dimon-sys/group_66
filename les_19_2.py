class Human:
    def __init__(self, name, color_of_hair, height, weight):
        self.name = name
        self.color_of_hair = color_of_hair
        self.height = height
        self.weight = weight


human1 = Human(name='Иван', color_of_hair='red', height=190, weight=90)
human1.name = 'Александр'
print(f'{human1.name} весит {human1.weight} кг при росте {human1.height} см')

human2 = Human(name='Савелий', color_of_hair='black', height=174, weight=90)
print(f'{human2.name} весит {human2.weight} кг при росте {human2.height} см')