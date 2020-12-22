# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

import inputs
import datetime
import re


def print_user_info(name, year, city, email, phone):
    print(f"name: {name}, year of birth: {year}, city: {city}, email: {email}, phone: {phone}")


if __name__ == "__main__":
    now = datetime.datetime.now()

    EMAIL_VALIDATION_PATTERN = r"^.+@.+\..{2,6}$"
    PHONE_VALIDATION_PATTERN = r"^\+?\d(-|\(|\s)?\d{3}(\)|-|\s)?-?\d{3}(-|\s)?\d{2}(-|\s)?\d{2}$"

    print_user_info(
        name = inputs.s('username', not_empty = True),
        year = inputs.i(
            'year of birth',
            validate_cb = lambda y: 1920 <= y <= now.year,
            error_message = f"Year of birth must be more 1920 and less {now.year}"
        ),
        city = inputs.s('city', not_empty = True),
        email = inputs.s(
            "email",
            validate_cb = lambda e: re.search(EMAIL_VALIDATION_PATTERN, e),
            error_message = "Invalid email format"
        ),
        phone = inputs.s(
            "phone",
            validate_cb = lambda p: re.search(PHONE_VALIDATION_PATTERN, p),
            exit_if_error = False,
            error_message = "Invalid phone format"
        )
    )
