# Звіт до роботи 2
### **Тема:** _Основи програмування на Python_

### **Мета роботи:** _Навчитися застосовувати основні конструкції мови Python, виконати всі приклади та за допомогою ChatGPT створити власні, які демонструють особливості кодових конструкцій Python._
---
### Виконання роботи

Оскільки всі завдання виконувалися у Python ноутбуці, необхідність у створенні скріншотів не має. Я створила [Python ноутбук](2.0.ipynb), у якому виконувала завдання з базовими конструкціями та прикладами програмування на мові Python. Використовуючи команду `print`, я виконала наступні кроки:

1. Ознайомилася з основними типами даних і попрацювала зі змінними таких типів, як `str` і `int`, а також із колекціями: списками (`list`), наборами (`set`), кортежами (`tuple`) та словниками (`dict`).
2. Вивчила три основні вбудовані константи в Python: `True`, `False`, і `None`. За допомогою функції `print` вивела значення  `True`.
3. Дослідила такі вбудовані функції, як `len()` для підрахунку кількості елементів у колекції, `sum()` для обчислення суми елементів, та `min()`, яка повертає найменше значення серед елементів.
4. Розібралася з циклами `for` і `while`, і з'ясувала що одну задачу можна вирішити обома способами. Також вивчила оператори `break` і `continue`, які використовуються для управління виконанням циклів.
5. Вивчила умовні конструкції `if` і дізналася, що в Python відсутній оператор `switch`, а умови зазвичай пишуться з `if`/`else`.
6. Опанувала конструкцію `try`, `except`, і `finally`, де останній блок завжди виконується, незалежно від наявності помилок.
7. Ознайомилася з контекст-менеджером `with`, який застосовується для узгодженого управління ресурсами, наприклад, під час роботи з файлами.
8. Дослідила лямбда-функції — анонімні функції, які можна написати в один рядок. Навів кілька прикладів для закріплення матеріалу.
---
Для перевірки своїх знань та прикладів коду я звернулася до ChatGPT, який надав пояснення щодо основ Python:

**Основи Python** включають важливі елементи:

1. **Змінні та типи даних**  
Python підтримує динамічну типізацію, тобто тип змінної вказувати не потрібно:

```python
x = 7  # int
y = 2.71  # float
name = "Angelina"  # str
```
Основні типи даних включають `int`, `float`, `str`, `list`, `tuple`, `set`, і `dict`.

2. **Оператори**  
Python має різні оператори для виконання дій: 
- арифметичні (`+`, `-`, `*`, `/`, `//`), 
- порівняльні (`==`, `!=`, `>`, `<`), 
- логічні (`and`, `or`, `not`).

3. **Умовні конструкції**  
За допомогою умовних операторів можна виконувати код залежно від умови:

```python
if x > 5:
    print("Greater than five")
elif x == 5:
    print("Equal to five")
else:
    print("Less than five")
```

4. **Цикли**  
Цикли дозволяють повторювати блок коду:

```python
for i in range(3):
    print(i)

while x > 0:
    x -= 1
```

5. **Функції**  
Функції дозволяють структурувати код і робити його більш зрозумілим:

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Angelina"))
```

6. **Обробка виключень**  
Для обробки помилок використовуються блоки `try-except`:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

7. **Модулі та бібліотеки**  
Python має безліч вбудованих бібліотек, які можна підключити за допомогою `import`:

```python
import random
print(random.randint(1, 20))
```

8. **Спискові включення (List comprehensions)**  
Це зручний спосіб створення списків:

```python
squares = [x**2 for x in range(5)]
```

---

### **Висновок:**

- ❓ **Що зроблено в роботі:** у процесі виконання лабораторної роботи я вивчила основні конструкції Python, включаючи змінні, оператори, умовні вирази, цикли та функції.😌
- ❓ **Чи досягнуто мети роботи:** мета роботи досягнута😁
- ❓ **Які нові знання отримано:** я познайомилася з основними типами даних і навчилася працювати з ними в Python. Також реалізувала приклади з використанням вбудованих функцій і лямбда-виразів, що допомогло мені закріпити основи програмування на Python.🙂
- ❓ **Чи вдалось відповісти на всі питання задані в ході роботи:** так, вдалося
- ❓**Чи вдалося виконати всі завдання:** вдалося виконати всі завдання😎
- ❓ **Чи виникли складності у виконанні завдання:** ні
- ❓**Чи подобається такий формат здачі роботи (Feedback):** так, такий формат мені подобається😄
- ❓ **Побажання для покращення (Suggestions):** немає
---