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


Client_1 = Client("Masha", "Shishkina", 25)
Client_2 = Client("Sasha", "Shishkin", 20)
Client_3 = Client("Fedor", "Romanov", 40)
Client_4 = Client("Elena", "Ivanova", 20)
Client_5 = Client("Filip", "Fedorov", 35)

print(f"There are next elements in class \'Client\':{Client_1}, {Client_2}, {Client_3}, {Client_4}, {Client_5}")


Animal_1 = Animal("Evgesha", "Crocodile", "green")
Animal_2 = Animal("Zhika", "Bear", "white")
Animal_3 = Animal("Snoop", "Wolf", "grey")
Animal_4 = Animal("Pushok", "Elephant", "grey")
Animal_5 = Animal("Stepan", "Giraffe", "yellow")

print(f"There are next elements in class \'Animal\':{Animal_1}, {Animal_2}, {Animal_3}, {Animal_4}, {Animal_5}")

Worker_1 = Worker("Maria", "Monday, Wednesday, Thursday, Sunday", "8.00 - 18.00")
Worker_2 = Worker("Gregory", "Monday, Tuesday, Friday, Saturday", "8.00 - 18.00")
Worker_3 = Worker("Vera", "Tuesday, Wednesday, Friday, Sunday", "12.00 - 22.00")
Worker_4 = Worker("Pablo", "Thursday, Friday, Saturday, Sunday", "12.00 - 22.00")
Worker_5 = Worker("Konstantin", "Tuesday, Friday, Saturday, Sunday", "12.00 - 22.00")

print(f"There are next elements in class \'Worker\':{Worker_1}, {Worker_2}, {Worker_3}, {Worker_4}, {Worker_5}")
