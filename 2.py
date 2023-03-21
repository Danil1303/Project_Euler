'''Каждый следующий элемент ряда Фибоначчи получается при сложении двух 
предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают 
четыре миллиона.'''

import time

sum = 0
list_of_fibonacci = []
first_number = int(input('Введите первый элемент' +
	 ' ряда Фибоначчи:\n'))
list_of_fibonacci.append(first_number)
second_number = int(input('Введите второй элемент' +
	' ряда Фибоначчи:\n'))
start_time = time.time()
if first_number % 2 == 0:
	sum += first_number
if second_number % 2 == 0:
	sum += second_number
list_of_fibonacci.append(second_number)
number = 0
while number < 4000000:
	if number % 2 == 0:
		sum += number
	number = list_of_fibonacci[-1] + list_of_fibonacci[-2]
	list_of_fibonacci.append(number)
print("--- %s seconds ---\n" % (time.time() - start_time))
# ~ print(list_of_fibonacci)
print(sum)

