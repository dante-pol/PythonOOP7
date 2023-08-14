class Client:
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age


Client_1 = Client("Masha", "Shishkina", 25)
Client_2 = Client("Sasha", "Shishkin", 20)
Client_3 = Client("Fedor", "Romanov", 40)
Client_4 = Client("Elena", "Ivanova", 20)
Client_5 = Client("Filip", "Fedorov", 35)


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

