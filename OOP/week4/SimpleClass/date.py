import json
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, Union

class Date:
    """
    Класс для работы с датами.
    Описание: Предоставляет функциональность для работы с датами, включая арифметические операции,
              преобразования и сохранение/загрузку в JSON.
    """
    
    def __init__(self, year: int, month: int, day: int):
        """
        Инициализация объекта Date.
        Параметры:
            year: Год (4 цифры)
            month: Месяц (1-12)
            day: День (1-31)
        """
        self._validate_date(year, month, day)
        self._year = year
        self._month = month
        self._day = day
    
    @property
    def year(self) -> int:
        """Геттер для года"""
        return self._year
    
    @property
    def month(self) -> int:
        """Геттер для месяца"""
        return self._month
    
    @property
    def day(self) -> int:
        """Геттер для дня"""
        return self._day
    
    @classmethod
    def from_string(cls, str_value: str) -> 'Date':
        """
        Создает объект Date из строки формата 'YYYY-MM-DD'.
        Параметры:
            str_value: Строка с датой
        Результат:
            Объект Date
        """
        try:
            year, month, day = map(int, str_value.split('-'))
            return cls(year, month, day)
        except (ValueError, AttributeError) as e:
            raise ValueError("Неверный формат строки. Ожидается 'YYYY-MM-DD'") from e
    
    def _validate_date(self, year: int, month: int, day: int) -> None:
        """Валидация даты"""
        if not (1 <= month <= 12):
            raise ValueError("Месяц должен быть от 1 до 12")
        
        max_days = 31
        if month in [4, 6, 9, 11]:
            max_days = 30
        elif month == 2:
            max_days = 29 if self._is_leap_year(year) else 28
        
        if not (1 <= day <= max_days):
            raise ValueError(f"День должен быть от 1 до {max_days} для месяца {month}")
    
    def _is_leap_year(self, year: int) -> bool:
        """Проверка на високосный год"""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    def to_datetime(self) -> datetime:
        """Преобразование в объект datetime"""
        return datetime(self._year, self._month, self._day)
    
    def day_of_week(self) -> str:
        """
        Возвращает день недели для даты.
        Результат:
            Название дня недели
        """
        days = ["Понедельник", "Вторник", "Среда", 
                "Четверг", "Пятница", "Суббота", "Воскресенье"]
        return days[self.to_datetime().weekday()]
    
    def is_weekend(self) -> bool:
        """
        Проверка, является ли день выходным.
        Результат:
            True если выходной, иначе False
        """
        return self.to_datetime().weekday() >= 5
    
    def days_until(self, other: 'Date') -> int:
        """
        Вычисляет количество дней между датами.
        Параметры:
            other: Объект Date для сравнения
        Результат:
            Количество дней между датами (всегда положительное)
        """
        delta = self.to_datetime() - other.to_datetime()
        return abs(delta.days)
    
    def __add__(self, other: Union[int, timedelta]) -> 'Date':
        """
        Сложение даты с числом дней или timedelta.
        Параметры:
            other: Количество дней или timedelta
        Результат:
            Новая дата
        """
        if isinstance(other, int):
            delta = timedelta(days=other)
        elif isinstance(other, timedelta):
            delta = other
        else:
            raise TypeError("Можно складывать только с int или timedelta")
        
        new_date = self.to_datetime() + delta
        return Date(new_date.year, new_date.month, new_date.day)
    
    def __sub__(self, other: Union['Date', int, timedelta]) -> Union[int, 'Date']:
        """
        Вычитание дат или дней из даты.
        Параметры:
            other: Дата, количество дней или timedelta
        Результат:
            Количество дней между датами или новая дата
        """
        if isinstance(other, Date):
            return self.days_until(other)
        elif isinstance(other, (int, timedelta)):
            return self.__add__(-other if isinstance(other, int) else -other)
        else:
            raise TypeError("Неверный тип операнда")
    
    def __eq__(self, other: 'Date') -> bool:
        """Проверка на равенство дат"""
        return self._year == other.year and self._month == other.month and self._day == other.day
    
    def __lt__(self, other: 'Date') -> bool:
        """Проверка, что текущая дата меньше другой"""
        return (self._year, self._month, self._day) < (other.year, other.month, other.day)
    
    def __str__(self) -> str:
        """Строковое представление даты"""
        return f"{self._year:04d}-{self._month:02d}-{self._day:02d}"
    
    def __call__(self) -> Dict[str, int]:
        """
        Вызываемый метод, возвращает дату в виде словаря.
        Результат:
            Словарь с ключами 'year', 'month', 'day'
        """
        return {'year': self._year, 'month': self._month, 'day': self._day}
    
    def save(self, filename: str) -> None:
        """
        Сохраняет дату в JSON-файл.
        Параметры:
            filename: Имя файла для сохранения
        """
        with open(filename, 'w') as f:
            json.dump(self(), f)
    
    @classmethod
    def load(cls, filename: str) -> 'Date':
        """
        Загружает дату из JSON-файла.
        Параметры:
            filename: Имя файла для загрузки
        Результат:
            Объект Date
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        return cls(data['year'], data['month'], data['day'])