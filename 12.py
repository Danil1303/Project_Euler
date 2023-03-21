'''
Третье треугольное число - 1+2+3=6, его делители - 1, 2, 3, 6.
Найти первое треугольное число, у которого более 500 делителей.
'''

from sieve_of_eratosthenes import sieve_of_eratosthenes


def func_12(target_dividers_amount: int) -> None:
    triangle_number = 0
    adder = 1
    primes = sieve_of_eratosthenes(500)
    while True:
        triangle_number += adder
        divider_list = [[]]
        x = triangle_number
        for divider in primes:
            if divider <= x:
                while x % divider == 0:
                    divider_list[-1].append(divider)
                    x /= divider
                if len(divider_list[-1]) != 0:
                    divider_list.append([])
            else:
                break
        if len(divider_list[-1]) == 0:
            divider_list = divider_list[:-1]

        dividers_amount = 1
        for i in divider_list:
            dividers_amount *= len(i) + 1
        if dividers_amount >= target_dividers_amount:
            print(f'Номер треугольного числа: {adder - 1}.')
            print(f'Само число: {triangle_number}.')
            print(f'Количество делителей: {dividers_amount}.')
            print(f'Список всех простых делителей: {divider_list}.')
            break
        adder += 1


func_12(500)
