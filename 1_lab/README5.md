# Звіт до роботи 5

### Тема: _Основні парадигми ООП_

### Мета роботи: _Ознайомитися з основними парадигмами об'єктно-орієнтованого програмування (ООП), зокрема інкапсуляцією, наслідуванням, поліморфізмом та абстракцією, а також набути практичні навички застосування цих принципів під час розробки програм_
------------------------------------------------------------------
## Основні парадигми ООП
Об'єктно-орієнтоване програмування (ООП) базується на кількох ключових парадигмах, які дозволяють організовувати програму у вигляді взаємодіючих об'єктів.
### 1. Інкапсуляція
Інкапсуляція означає приховування деталей реалізації об'єкта, забезпечуючи доступ до них лише через спеціальні методи. В Python інкапсуляція реалізується за допомогою:

- Публічних атрибутів і методів (public): доступні звідусіль.
- Приватних атрибутів і методів (private): позначаються символом _ або __ (наприклад, _attr, __attr).

Приклад:
```py
class EWallet:
    def __init__(self, owner, balance):
        self.owner = owner  
        self.__balance = balance  
        self.__bonus = 0  

    def add_funds(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__bonus += amount * 0.05

    def spend_funds(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"Spent {amount} units"
        else:
            return "Not enough balance"

    def get_balance_info(self):
        return f"Balance: {self.__balance} units, Bonus: {self.__bonus:.2f} units"

wallet = EWallet("Angelina", 300)
wallet.add_funds(200)
print(wallet.get_balance_info())  00 units
wallet.spend_funds(150)
print(wallet.get_balance_info())  

```
Результат програми:
```py
Balance: 500 units, Bonus: 10.00 units
Balance: 350 units, Bonus: 10.00 units
```
- Ця програма створює клас EWallet, який представляє електронний гаманець з власником, балансом і бонусами. Баланс і бонус приховані (приватні атрибути) й доступні тільки через методи. Метод add_funds() поповнює гаманець і додає 5% від суми в бонуси, spend_funds() дозволяє витратити гроші, якщо їх достатньо, а get_balance_info() повертає інформацію про баланс і бонуси.

### 2. Наслідування
**Наслідування** — це один з основних принципів об'єктно-орієнтованого програмування, який дозволяє створювати нові класи на основі вже існуючих. При цьому новий клас, який називається дочірнім, успадковує всі атрибути та методи базового класу, що дозволяє повторно використовувати код і створювати більш спеціалізовані класи.

Приклад:
```py
class LibraryAccount:
    def __init__(self, user_name):
        self.user_name = user_name 
        self.__borrowed_books = []  
    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)
            return f"Returned '{book_title}'"
        else:
            return f"No such book borrowed"

    def list_borrowed_books(self):
        return f"Borrowed books: {', '.join(self.__borrowed_books) if self.__borrowed_books else 'None'}"

account = LibraryAccount("Angelina")
account.borrow_book("Python Programming")
account.borrow_book("Data Science 101")
print(account.list_borrowed_books())
print(account.return_book("Python Programming"))
print(account.list_borrowed_books())
```
Результат програми:
```py
Borrowed books: Python Programming, Data Science 101
Returned 'Python Programming'
Borrowed books: Data Science 101
```
- Програма створює клас LibraryAccount, який зберігає ім'я користувача та список позичених книг. Список книг прихований від прямого доступу. Метод borrow_book() додає нову книгу, return_book() видаляє книгу зі списку, а list_borrowed_books() повертає всі книги, які зараз позичені.

### 3. Поліморфізм
Поліморфізм означає, що одна і та сама дія може виконуватись по-різному в залежності від об'єкта. Це забезпечується за допомогою перевизначення методів.

Приклад:
```py
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())

```
Результат програми:
```
Woof!
Meow!
```
- У цьому прикладі створено базовий клас Animal із методом speak(), який нічого не робить. Класи Dog і Cat успадковують Animal і перевизначають метод speak() по-своєму: Dog повертає "Woof!", а Cat — "Meow!". Завдяки поліморфізму в циклі можна викликати speak() для кожного об'єкта без уточнення його типу, і кожен об'єкт виконує свою версію методу.

### 4. Абстракція
Абстракція приховує складність та залишає лише необхідні деталі. В Python це реалізується через абстрактні класи (використовуючи модуль abc).

Приклад:
```py
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())  # 78.5
```
Результат програми:
```
78.5
```
- У цьому прикладі створено абстрактний клас Shape з абстрактним методом area(), який не має реалізації. Клас Circle успадковує Shape і обов'язково реалізує власну версію методу area(), що обчислює площу круга за формулою \( \pi r^2 \). Абстракція дозволяє визначити спільний інтерфейс для різних фігур, залишаючи деталі реалізації кожному підкласу.

Висновок:

- ❓ Що зроблено в роботі: Ознайомилися з парадигмами в ООП
- ❓ Чи досягнуто мети роботи: Мета роботи досягнута
- ❓ Які нові знання отримано: Чим відрізняються кожна парадигма між собою
- ❓ Чи вдалось відповісти на всі питання задані в ході роботи: Так, вдалося
- ❓ Чи вдалося виконати всі завдання: Вдалося виконати всі завдання
- ❓ Чи виникли складності у виконанні завдання: Складностей не виникло
- ❓ Чи подобається такий формат здачі роботи (Feedback): Так, такий формат здачі робіт мені до вподоби
- ❓ Побажання для покращення (Suggestions): Немає
