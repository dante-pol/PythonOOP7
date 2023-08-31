class Computer:
    def __init__(self, brand, model, cpu, ram, storage):
        self.__brand = brand
        self.__model = model
        self.__cpu = cpu
        self.__ram = ram
        self.__storage = storage
        self.is_on = False
        self.software = []

    def turn_on(self):
        self.is_on = True
        print("Компьютер включен")

    def turn_off(self):
        self.is_on = False
        print("Компьютер выключен")

    def install_software(self, software_name):
        if not self.is_on:
            print("Компьютер выключен. Установка программы невозможна.")
            return
        self.software.append(software_name)
        print(f"Установлена программа {software_name}")

    def describe(self):
        print(f"Марка: {self.__brand}\nМодель: {self.__model}\nПроцессор: {self.__cpu}\nОперативная память: {self.__ram} ГБ\nХранилище: {self.__storage} ГБ")
        print(f"Состояние питания: {'включен' if self.is_on else 'выключен'}")
        print("Установленные программы:", ', '.join(self.software))

# Пример использования класса
comp = Computer("Apple", "MacBook Pro", "Intel Core i7", 16, 512)
comp.turn_on()
comp.install_software("Microsoft Office")
comp.describe()
comp.turn_off()