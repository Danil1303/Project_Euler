'''Если выписать все натуральные числа меньше 10, кратные 3 или 5, 
то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.'''

import time

r = int(input('Введите число, до которого будут выполняться расчёты:\n'))
start_time = time.time()
print('\n')
sum = 0
for i in range(1, r):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)
print("--- %s seconds ---\n" % (time.time() - start_time))
