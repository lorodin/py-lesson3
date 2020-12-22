# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

import inputs


def div(n, d):
    try:
        return n / d
    except ZeroDivisionError:
        print("Denominator is zero")


if __name__ == "__main__":
    a = inputs.f("numerator")
    b = inputs.f("denominator")
    result = div(a, b)
    if result:
        print(f"a / b = { result }")
