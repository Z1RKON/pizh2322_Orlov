from typing import List, Dict, Union, Optional
import json
from date import Date

class DateContainer:
    """
    Класс-контейнер для хранения и управления коллекцией объектов Date.
    Описание: Предоставляет функциональность для работы с коллекцией дат,
              включая добавление, удаление, индексацию и сохранение/загрузку.
    """
    
    def __init__(self, initial_data: Optional[List[Date]] = None):
        """
        Инициализация контейнера.
        Параметры:
            initial_data: Начальный список объектов Date (по умолчанию None)
        """
        self._data: List[Date] = initial_data.copy() if initial_data else []
    
    @property
    def data(self) -> List[Date]:
        """Геттер для доступа к данным (только чтение)"""
        return self._data.copy()
    
    def add(self, value: Date) -> None:
        """
        Добавляет объект Date в контейнер.
        Параметры:
            value: Объект Date для добавления
        """
        if not isinstance(value, Date):
            raise TypeError("Можно добавлять только объекты Date")
        self._data.append(value)
    
    def remove(self, index: int) -> Date:
        """
        Удаляет и возвращает объект Date по индексу.
        Параметры:
            index: Индекс удаляемого элемента
        Результат:
            Удаленный объект Date
        """
        if not 0 <= index < len(self._data):
            raise IndexError("Индекс вне диапазона")
        return self._data.pop(index)
    
    def __getitem__(self, key: Union[int, slice]) -> Union[Date, List[Date]]:
        """
        Поддержка индексации и срезов.
        Параметры:
            key: Индекс или срез
        Результат:
            Объект Date или список Date
        """
        return self._data[key]
    
    def __len__(self) -> int:
        """Возвращает количество элементов в контейнере"""
        return len(self._data)
    
    def __str__(self) -> str:
        """Строковое представление контейнера"""
        return f"DateContainer с {len(self)} датами: " + ", ".join(str(d) for d in self._data)
    
    def __call__(self) -> List[Dict[str, int]]:
        """
        Вызываемый метод, возвращает данные в формате, пригодном для JSON.
        Результат:
            Список словарей с датами
        """
        return [date() for date in self._data]
    
    def save(self, filename: str) -> None:
        """
        Сохраняет контейнер в JSON-файл.
        Параметры:
            filename: Имя файла для сохранения
        """
        with open(filename, 'w') as f:
            json.dump(self(), f, indent=2)
    
    @classmethod
    def load(cls, filename: str) -> 'DateContainer':
        """
        Загружает контейнер из JSON-файла.
        Параметры:
            filename: Имя файла для загрузки
        Результат:
            Новый объект DateContainer
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        
        container = cls()
        for item in data:
            container.add(Date(item['year'], item['month'], item['day']))
        return container