from __future__ import annotations
from typing import Union

class Roman:
    """
    Класс Roman представляет римское число и поддерживает операции +, -, *, /.
    Описание: Этот класс позволяет создавать объекты римских чисел, выполнять арифметические операции
    и преобразовывать числа между арабскими и римскими форматами.
    """

    # Статический словарь для преобразования римских чисел в арабские
    _ROMAN_TO_ARABIC = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    # Статический словарь для преобразования арабских чисел в римские
    _ARABIC_TO_ROMAN = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    def __init__(self, value: Union[str, int]):
        """
        Инициализация экземпляра класса Roman.
        Параметры:
        - value: строка (римское число) или целое число (арабское число).
        """
        if isinstance(value, str):
            self._value = self._roman_to_arabic(value)
        elif isinstance(value, int):
            self._value = value
        else:
            raise ValueError("Недопустимый тип данных для инициализации.")

    @property
    def value(self) -> int:
        """
        Возвращает арабское значение римского числа.
        Результат: целое число.
        """
        return self._value

    @staticmethod
    def _roman_to_arabic(roman: str) -> int:
        """
        Преобразует римское число в арабское.
        Параметры:
        - roman: строка, представляющая римское число.
        Результат: целое число.
        """
        total = 0
        prev_value = 0
        for char in reversed(roman):
            value = Roman._ROMAN_TO_ARABIC[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total

    @staticmethod
    def _arabic_to_roman(arabic: int) -> str:
        """
        Преобразует арабское число в римское.
        Параметры:
        - arabic: целое число.
        Результат: строка, представляющая римское число.
        """
        if arabic <= 0:
            raise ValueError("Римские числа могут быть только положительными.")
        result = []
        for num, symbol in Roman._ARABIC_TO_ROMAN:
            while arabic >= num:
                result.append(symbol)
                arabic -= num
        return ''.join(result)

    def __add__(self, other: Roman) -> Roman:
        """
        Сложение двух римских чисел.
        Параметры:
        - other: экземпляр класса Roman.
        Результат: новый экземпляр класса Roman.
        """
        return Roman(self._value + other._value)

    def __sub__(self, other: Roman) -> Roman:
        """
        Вычитание двух римских чисел.
        Параметры:
        - other: экземпляр класса Roman.
        Результат: новый экземпляр класса Roman.
        """
        return Roman(self._value - other._value)

    def __mul__(self, other: Roman) -> Roman:
        """
        Умножение двух римских чисел.
        Параметры:
        - other: экземпляр класса Roman.
        Результат: новый экземпляр класса Roman.
        """
        return Roman(self._value * other._value)

    def __truediv__(self, other: Roman) -> Roman:
        """
        Деление двух римских чисел.
        Параметры:
        - other: экземпляр класса Roman.
        Результат: новый экземпляр класса Roman.
        """
        return Roman(self._value // other._value)

    def __call__(self) -> str:
        """
        Вызываемый метод для получения римского числа.
        Результат: строка, представляющая римское число.
        """
        return self._arabic_to_roman(self._value)

    def __str__(self) -> str:
        """
        Возвращает строковое представление римского числа.
        Результат: строка.
        """
        return self._arabic_to_roman(self._value)

# Пример использования
if __name__ == "__main__":
    r1 = Roman("X")
    r2 = Roman(5)

    print(f"r1: {r1()}")  # r1: X
    print(f"r2: {r2()}")  # r2: V

    r3 = r1 + r2
    print(f"r1 + r2: {r3()}")  # r1 + r2: XV

    r4 = r1 - r2
    print(f"r1 - r2: {r4()}")  # r1 - r2: V

    r5 = r1 * r2
    print(f"r1 * r2: {r5()}")  # r1 * r2: L

    r6 = r1 / r2
    print(f"r1 / r2: {r6()}")  # r1 / r2: II