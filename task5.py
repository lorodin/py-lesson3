# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.

import inputs

EXIT_CODE = 'e'
g_close = False


def line_numbers(text):
    global g_close
    items = text.split(' ')
    for item in items:
        if item.isdigit():
            yield int(item)
        elif item == EXIT_CODE:
            g_close = True
            return


if __name__ == '__main__':
    total_sum = 0
    while not g_close:
        line = inputs.s(f'Enter numbers separated by space ({ EXIT_CODE } - for exit)', not_empty = False)
        total_sum += sum(line_numbers(line))
        print(f'Total sum: { total_sum }')
