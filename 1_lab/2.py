import random

# Генерація випадкового числа від 1 до 100
secret_number = random.randint(1, 100)
attempts = 0
guess = 0

print("Я загадав число від 1 до 100. Спробуй вгадати його!")

# Основний цикл гри
while guess != secret_number:
    guess = int(input("Введи своє припущення: "))
    attempts += 1
    
    if guess < secret_number:
        print("Загадане число більше.")
    elif guess > secret_number:
        print("Загадане число менше.")
    else:
        print(f"Вітаю! Ти вгадав число {secret_number} за {attempts} спроб.")

