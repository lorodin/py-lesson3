# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
#
# ** Подсказка:** попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

import inputs


def custom_pow(x, y):
    val = 1
    for i in range(abs(y)):
        val *= x
    return 1 / val


if __name__ == "__main__":
    print("Input x ** y")
    x = inputs.i("x", positive_only = True, error_message = "X must be more 0")
    y = inputs.i(
        "y",
        validate_cb = lambda v: v < 0,
        error_message = "Y must be less 0"
    )
    print(f"          x ** y = { x ** y }")
    print(f"custom_pow(x, y) = { custom_pow(x, y) }")
