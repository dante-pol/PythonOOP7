class Client:
    def __init__(self, first_name: str, second_name: str, age: int) -> None:
        self.__first_name = first_name
        self.__second_name = second_name
        self.__age = age

    def __str__(self) -> str:
        return f"Name: {self.__first_name}, Second_name: " \
               f"{self.__second_name}, Age: {self.__age}"


class Animal:
    def __init__(self, type: str, color: str, name: str) -> None:
        self.__name = name
        self.__type = type
        self.__color = color

    def __str__(self) -> str:
        return f"Name: {self.__name}, Type: {self.__type}, " \
               f"Color: {self.__color}"


class Worker:
    def __init__(self, name: str,
                 visiting_day: str,
                 visiting_time: str) -> None:
        self.__name = name
        self.visiting_day = visiting_day
        self.visiting_time = visiting_time

    def __str__(self) -> str:
        return f"Name: {self.__name}, Visiting_day: {self.visiting_day}," \
               f" Cisiting_time: {self.visiting_time}"


Client_1 = Client("Masha", "Shishkina", 25)
Client_2 = Client("Sasha", "Shishkin", 20)
Client_3 = Client("Fedor", "Romanov", 40)
Client_4 = Client("Elena", "Ivanova", 20)
Client_5 = Client("Filip", "Fedorov", 35)

print(f"There are next elements in class \'Client\':\n{Client_1},\n"
      f"{Client_2},\n{Client_3},\n{Client_4},\n{Client_5}")
print()

Animal_1 = Animal("Evgesha", "Crocodile", "green")
Animal_2 = Animal("Zhika", "Bear", "white")
Animal_3 = Animal("Snoop", "Wolf", "grey")
Animal_4 = Animal("Pushok", "Elephant", "grey")
Animal_5 = Animal("Stepan", "Giraffe", "yellow")

print(f"There are next elements in class \'Animal\':\n{Animal_1},\n"
      f"{Animal_2},\n{Animal_3},\n{Animal_4},\n{Animal_5}")
print()

Worker_1 = Worker("Maria", "Monday, Wednesday, "
                  "Thursday, Sunday", "8.00 - 18.00")
Worker_2 = Worker("Gregory", "Monday, Tuesday, Friday,"
                  " Saturday", "8.00 - 18.00")
Worker_3 = Worker("Vera", "Tuesday, Wednesday, Friday,"
                  " Sunday", "12.00 - 22.00")
Worker_4 = Worker("Pablo", "Thursday, Friday, Saturday,"
                  " Sunday", "12.00 - 22.00")
Worker_5 = Worker("Konstantin", "Tuesday, Friday, Saturday,"
                  " Sunday", "12.00 - 22.00")

print(f"There are next elements in class \'Worker\':\n{Worker_1},\n"
      f"{Worker_2},\n{Worker_3},\n{Worker_4},\n{Worker_5}")
