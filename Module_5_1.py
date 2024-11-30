class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def __del__(self):
        print(f'"{self.name}" снесён, но он останется в истории')

    def go_to (self, new_floor):
        if 1 <= int(new_floor) <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: "{self.name}", кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self


building1 = House('Монохром', 25)
print(House.houses_history)
building2 = House('Кругляк', 9)
print(House.houses_history)
building3 = House('Дикий-Дом', 7)
print(House.houses_history)
building4 = House('Каменьщик', 5)
print(House.houses_history)

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

print(building1 == building2) # __eq__
building2 = building2 + 16 # __add__
print(building2)
print(building1 == building2)
building3 += 8 # __iadd__
print(building3)
building4 = 10 + building4 # __radd__
print(building4)
print(building1 > building2) # __gt__
print(building1 >= building2) # __ge__
print(building3 < building4) # __lt__
print(building3 <= building4) # __le__
print(building2 != building4) # __ne__

del building3
del building1

print(House.houses_history)