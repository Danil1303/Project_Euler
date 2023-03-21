'''Число-палиндром с обеих сторон (справа налево и слева направо) 
читается одинаково. Самое большое число-палиндром, полученное 
умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух 
трехзначных чисел.'''

import time

start_time = time.time()
minimum = 100
# Для ускорения выччислений сделаем min = 900:
minimum = 900
maximum = 999
list_of_palindroms = []
for i in range(minimum, maximum + 1):
	for j in range(minimum, maximum + 1):
		palindrom = i * j
		list_palindrom = list(str(palindrom))
		if (list_palindrom[0] == list_palindrom[-1]
			and list_palindrom[1] == list_palindrom[-2]
			and list_palindrom[2] == list_palindrom[-3]):
			list_of_palindroms.append(palindrom)
print(max(list_of_palindroms))
print(list_of_palindroms)
print("--- %s seconds ---\n" % (time.time() - start_time))

