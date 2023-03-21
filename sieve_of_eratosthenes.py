from itertools import repeat
from math import sqrt, ceil


def sieve_of_eratosthenes(number: int) -> list[int]:
    sieve = number * [True]
    for i in range(3, int(sqrt(number)), 2):
        sieve[2 * i::i] = repeat(False, (ceil(number / i)) - 2)
    list_of_prime_numbers = [2] + [p for p in (i for i in range(3, number, 2) if sieve[i])]
    return list_of_prime_numbers

# First version

# def sieve_of_eratosthenes(number):
#     list_of_prime_numbers = [i for i in range(2, number)]
#     for i in list_of_prime_numbers:
#         for j in list_of_prime_numbers[i-1:]:
#             if j%i==0:
#                 list_of_prime_numbers.remove(j)
#     return list_of_prime_numbers
