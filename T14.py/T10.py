#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной 
# и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Ведите число монет на столе:'))
count_zero = 0
count_one = 0
for i in range(n):
   x = int(input('Ведите позицию монеты где решка это - 0, а орел - 1: '))
   if x == 0:
     count_zero += 1
else:
     count_one += 1
if count_one > count_zero:
   print('Минимальное количество монет, которые нужно перевернуть -', count_zero)
else:
   print('Минимальное количество монет, которые нужно перевернуть -', count_one) 
