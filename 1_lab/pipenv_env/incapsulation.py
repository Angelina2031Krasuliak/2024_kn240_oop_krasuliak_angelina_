from bank import BankAccount

account = BankAccount("Іван", 1000)
print(account.owner)  

account.deposit(500)
account.withdraw(300)
print("Поточний баланс:", account.get_balance())

print("Прямий доступ:", account._BankAccount__balance) 