#Задача 10 На столе лежат n монеток. Некоторые из них лежат вверх решкой, а 
# некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное 
# количество монет, которые нужно перевернуть   Пример  5  -> 1 0 1 1 0  ->  2

import random
tails = 0
heads = 1
count = 0
quantity = int(input('Введите количество монеток: '))

for i in range (quantity):
    randNumber = random.randint(0, 1)
    print(randNumber, end=" ")
    if randNumber > 0:
        count += 1

print (' Минимальное количество монет, которые нужно перевернуть:', 
count if count < (quantity-count) else (quantity-count))