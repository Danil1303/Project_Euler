'''
n-чётное, n=n/2
n-нечётное, n=3n+1
Последовательность, начиная с 13: 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.
Какой начальный элемент меньше 1000000 генерирует самую длинную последовательность?
'''


def func_12(limit: int) -> None:
    max_sequence_list = []
    for number in range(3, limit + 1):
        sequence_list = []
        sequence_list.append(number)
        while number != 1:
            if number % 2 == 0:
                number = int(number / 2)
            else:
                number = 3 * number + 1
            sequence_list.append(number)
        if len(sequence_list) > len(max_sequence_list):
            max_sequence_list = (sequence_list)

    print(max_sequence_list[0])
    print(len(max_sequence_list))
    print(max_sequence_list)


func_12(500000)

def generator

# def func_12(limit: int) -> None:
#     numbers_list = [i for i in range(3, limit + 1)]
#     max_sequence_list = []
#     while True:
#         number = numbers_list[0]
#         sequence_list = []
#         sequence_list.append(number)
#         while number != 1:
#             try:
#                 numbers_list.remove(number)
#             except ValueError:
#                 pass
#             if number % 2 == 0:
#                 number = number / 2
#             else:
#                 number = 3 * number + 1
#             sequence_list.append(number)
#         if len(sequence_list) > len(max_sequence_list):
#             max_sequence_list = (sequence_list)
#         if len(numbers_list)==0:
#             break
#
#     print(max_sequence_list[0])
#     print(len(max_sequence_list))
#     print(max_sequence_list)

