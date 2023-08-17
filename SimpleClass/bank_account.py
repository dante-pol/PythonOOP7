class BankAccount:
    def __init__(self, owner, balance=0):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        if amount <= 0:
            print("Сумма вклада должна быть положительной")
            return
        self.balance += amount
        print(f"Внесено {amount} у.е. на счет")

    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма снятия должна быть положительной")
            return
        if amount > self.balance:
            print("Недостаточно средств на счете")
            return
        self.balance -= amount
        print(f"Снято {amount} у.е. со счета")

    def get_balance(self):
        return self.balance

    def describe(self):
        print(f"Владелец счета: {self.owner}\nБаланс счета: {self.balance} у.е.")

# Пример использования класса
account = BankAccount("Иван", 1000)
account.deposit(500)
account.withdraw(200)
account.describe()
print(f"Текущий баланс: {account.get_balance()} у.е.")
