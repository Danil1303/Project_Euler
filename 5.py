'''2520 - самое маленькое число, которое делится без остатка на все числа 
от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?'''

import time

start_time = time.time()
list1 = []
flag = 0
number = 1
minimum = 1
maximum = 12
list1 = list(range(minimum, maximum + 1))
while True:
	for n in list1:
		if number % n == 0:
			flag += 1
	if flag == (maximum - minimum + 1):
		print(number)
		break
	number += 1
	flag = 0
print('--- %s seconds ---\n' % (time.time() - start_time))
