'''
Какое число является 10001-м простым числом?
'''

from sieve_of_eratosthenes import sieve_of_eratosthenes

def func_7(prime_number = 10001):
    primes_list = sieve_of_eratosthenes(10000000)
    print(primes_list[prime_number-1])

func_7()