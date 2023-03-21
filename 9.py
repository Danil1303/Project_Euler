'''
Существует только одна Пифагорова тройка, для которой a+b+c=1000. Найти abc.

a = m^2-n^2
b = 2mn
c = m^2+n^2
a+b+c = m^2-n^2 + 2mn + m^2+n^2
a+b+c = 2*(m^2) + 2mn = m^2 + mn = 500
'''


def func_9():
    for m in range(1000):
        for n in range(1000):
            if (m * m + m * n) == 500:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                if a > 0 and b > 0 and c > 0:
                    print(f'Числа: {a = }, {b = }, {c = }.')
                    print(f'Произведение: {a * b * c}.')


func_9()