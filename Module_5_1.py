class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to (self, new_floor):
        if not isinstance(self.number_of_floors, int):
            print('Введите правильный номер этажа')
        elif 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует")

building1 = House('Монохром', 25)
building2 = House('Кругляк', 9)
building3 = House('Дикий-Дом', "l")
building4 = House('Каменьщик', 5)

building1.go_to(13)
building2.go_to(0)
building3.go_to(7)
building4.go_to(9)