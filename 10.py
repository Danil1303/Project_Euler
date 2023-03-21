'''
Найдите сумму всех простых чисел меньше двух миллионов.
'''

from sieve_of_eratosthenes import sieve_of_eratosthenes


def func_10(number: int) -> int:
    primes_list = sieve_of_eratosthenes(number)
    primes_sum = sum(primes_list)
    return primes_sum


print(func_10(2000000))
