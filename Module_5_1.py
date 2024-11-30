class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to (self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: "{self.name}", кол-во этажей: {self.number_of_floors}'

building1 = House('Монохром', 25)
building2 = House('Кругляк', 9)
building3 = House('Дикий-Дом', 7)
building4 = House('Каменьщик', 5)

building1.go_to(13)
building2.go_to(0)
building3.go_to(3)
building4.go_to(9)

print(building1)
print(building2)
print(building3)
print(building4)

print(len(building1))
print(len(building2))
print(len(building3))
print(len(building4))