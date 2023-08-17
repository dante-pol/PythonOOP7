class OnlineStore:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.customers = []
        self.orders = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def register_customer(self, customer):
        self.customers.append(customer)

    def create_order(self, customer, product):
        if customer in self.customers and product in self.products:
            self.orders.append((customer, product))
        else:
            print("Ошибка при создании заказа: клиент или продукт не найден")

    def describe(self):
        print(f"Магазин: {self.name}")
        print("Продукты:")
        for product in self.products:
            print(f"- {product}")
        print("Клиенты:")
        for customer in self.customers:
            print(f"- {customer}")
        print("Заказы:")
        for order in self.orders:
            print(f"- {order[0]} заказал {order[1]}")

# Пример использования класса
store = OnlineStore("Продуктовый магазин")
store.add_product("Молоко")
store.add_product("Хлеб")
store.register_customer("Иван")
store.register_customer("Анна")
store.create_order("Иван", "Молоко")
store.create_order("Анна", "Хлеб")
store.describe()
