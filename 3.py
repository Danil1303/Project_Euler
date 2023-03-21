'''Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?'''

import time
import math

number = 13195123
list1 = []

''' Первый вариант.'''
start_time = time.time()
list1 = []
flag = 0
for i in range(1, number):
	if number % i == 0:
		for j in range(1, i + 1):
			if i % j == 0:
				flag += 1
		if flag == 2:
			list1.append(i)
		flag = 0			
print('Наибольший простой делитель: ' + str(max(list1)) + '.')
print(list1)
print("--- %s seconds ---\n" % (time.time() - start_time))

''' Оптимизированный вариант.'''
start_time = time.time()
list1 = []
flag = 0
# math.floor(math.sqrt(number)) - округление в меньшую сторону корня числа. 
#Наибольший делитель не может встретиться среди чисел больше квадратного корня 
#от проверяемого.
for i in range(2, math.floor(math.sqrt(number))):
	if number % i == 0:
		list1.append(i)
list1.reverse()
for n in list1:
	for j in range(1, list1[0] + 1):
		if n % j == 0:
			flag += 1
	if flag == 2:
		print('Наибольший простой делитель: ' + str(n) + '.')
		break
	flag = 0		
print(list1)
print("--- %s seconds ---\n" % (time.time() - start_time))

''' Решение при помощи решета Эратосфена'''
start_time = time.time()
list1 = []
for i in range(2, math.floor(math.sqrt(number))):
	if number % i == 0:
		list1.append(i)
for p in list1:
	for n in list1:
		if n % p == 0:
			list1.remove(n)
print('Наибольший простой делитель: ' + str(max(list1)) + '.')
print(list1)
print("--- %s seconds ---\n" % (time.time() - start_time))

