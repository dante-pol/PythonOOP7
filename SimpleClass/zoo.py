class Client:
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age


class Animal:
    def __init__(self, type, color, name):
        self.name = name
        self.type = type
        self.color = color


class Worker:
    def __init__(self, name, visiting_day, visiting_time):
        self.name = name
        self.visiting_day = visiting_day
        self.visiting_time = visiting_time


man = Client("Ivan", "Ivanov", 33)
cat = Animal("tiger", "ginger", "busik")
man_2 = Worker("Piter", "monday", "12:00")
print(f"Возраст посетителя :{man.age} года")
print(F"в нашем зоопарке есть {cat.type} по имени {cat.name}")
print(f"Дрессировщика {cat.type} зовут {man_2.name}")
