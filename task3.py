# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

import inputs


def my_func(n_1, n_2, n_3):
    return max(n_1 + n_2, n_2 + n_3, n_1 + n_3)


if __name__ == "__main__":
    print("Input numbers")
    n1 = inputs.f("[1]")
    n2 = inputs.f("[2]")
    n3 = inputs.f("[3]")
    print(f"Mux numbers sum: { my_func(n1, n2, n3) }")
