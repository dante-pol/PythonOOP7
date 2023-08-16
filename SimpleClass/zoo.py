class Client:
    def __init__(self, first_name: str, second_name: str, age: int) -> None:
        self.first_name: str = first_name
        self.second_name: str = second_name
        self.age: int = age

    def get_info(self) -> str:
        return f"Name: {self.first_name} {self.second_name}, Age: {self.age}"


class Animal:
    def __init__(self, name: str, color: str, type: str) -> None:
        self.name: str = name
        self.color: str = color
        self.type: str = type

    def get_info(self) -> str:
        return f"Name: {self.name}, Color: {self.color}, Type: {self.type} "


class Worker:
    def __init__(self, name: str, visiting_day: str, visiting_time: str) -> None:
        self.name: str = name
        self.visiting_day: str = visiting_day
        self.visiting_time: str = visiting_time

    def get_info(self) -> str:
        return f"Name: {self.name}, Visiting days: {self.visiting_day}, Visiting time: {self.visiting_time}"


Client_1: Client = Client(first_name="Masha", second_name="Shishkina", age=25)
Client_2: Client = Client(first_name="Sasha", second_name="Shishkin", age=20)
Client_3: Client = Client(first_name="Fedor", second_name="Romanov", age=40)
Client_4: Client = Client(first_name="Elena", second_name="Ivanova", age=20)
Client_5: Client = Client(first_name="Filip", second_name="Fedorov", age=35)

print("There are next elements in class 'Client':")
print(Client_1.get_info())
print(Client_2.get_info())
print(Client_3.get_info())
print(Client_4.get_info())
print(Client_5.get_info())


Animal_1: Animal = Animal(name="Evgesha", color="green", type="Crocodile")
Animal_2: Animal = Animal(name="Zhika", color="white", type="Bear")
Animal_3: Animal = Animal(name="Snoop", color="grey", type="Wolf")
Animal_4: Animal = Animal(name="Pushok", color="grey", type="Elephant")
Animal_5: Animal = Animal(name="Stepan", color="yellow", type="Giraffe")

print("There are next elements in class 'Animal':")
print(Animal_1.get_info())
print(Animal_2.get_info())
print(Animal_3.get_info())
print(Animal_4.get_info())
print(Animal_5.get_info())

Worker_1: Worker = Worker(
    name="Maria",
    visiting_day="Monday, Wednesday, Thursday, Sunday",
    visiting_time="8.00 - 18.00",
)
Worker_2: Worker = Worker(
    name="Gregory",
    visiting_day="Monday, Tuesday, Friday, Saturday",
    visiting_time="8.00 - 18.00",
)
Worker_3: Worker = Worker(
    name="Vera",
    visiting_day="Tuesday, Wednesday, Friday, Sunday",
    visiting_time="12.00 - 22.00",
)
Worker_4: Worker = Worker(
    name="Pablo",
    visiting_day="Thursday, Friday, Saturday, Sunday",
    visiting_time="12.00 - 22.00",
)
Worker_5: Worker = Worker(
    name="Konstantin",
    visiting_day="Tuesday, Friday, Saturday, Sunday",
    visiting_time="12.00 - 22.00",
)

print("There are next elements in class 'Worker':")
print(Worker_1.get_info())
print(Worker_2.get_info())
print(Worker_3.get_info())
print(Worker_4.get_info())
print(Worker_5.get_info())
