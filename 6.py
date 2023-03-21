# Найдите разность между суммой квадратов и квадратом суммы.

def squares_difference(number):
    summ_of_squares = sum([x**2 for x in range(1, number + 1)])
    square_of_summ= sum([x for x in range(1, number +1)])**2
    print(f'Разность: {square_of_summ-summ_of_squares}.')

number = int(input('Количество чисел: '))
squares_difference(number)