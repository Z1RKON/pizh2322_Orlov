from abc import ABC, abstractmethod
from typing import Any


class Animal(ABC):
    """Абстрактный базовый класс для животных.
    
    Описание:
        Этот класс определяет абстрактный метод `to_answer()`, который должен быть реализован в подклассах."""
    
    @abstractmethod
    def to_answer(self) -> str:
        """Абстрактный метод для генерации ответа животного.
        
        Результат:
            str: Ответ животного в виде строки."""
        pass


class Kitten(Animal):
    """Класс, представляющий котенка, который может отвечать на вопросы.
    
    Описание:
        Котенок чередует ответы "да" и "нет", начиная с "да". 
        Подсчитывает количество ответов каждого типа."""
    
    def __init__(self, name: str) -> None:
        """Инициализирует экземпляр класса Kitten.
        
        Параметры:
            name (str): Имя котенка."""
        self.name = name
        self._yes_count: int = 0
        self._no_count: int = 0
        self._next_answer: bool = True  # Флаг для определения следующего ответа (True = "да")
    
    def to_answer(self) -> str:
        """Генерирует ответ котенка, чередуя "да" и "нет".
        
        Результат:
            str: "moore-moore" для "да", "meow-meow" для "нет"."""
        if self._next_answer:
            self._yes_count += 1
            response = "moore-moore"
        else:
            self._no_count += 1
            response = "meow-meow"
        self._next_answer = not self._next_answer
        return response
    
    def number_yes(self) -> int:
        """Возвращает количество ответов "да".
        
        Результат:
            int: Количество ответов "да"."""
        return self._yes_count
    
    def number_no(self) -> int:
        """Возвращает количество ответов "нет".
        
        Результат:
            int: Количество ответов "нет"."""
        return self._no_count


class Owner:
    """Класс, представляющий владельца котенка.
    
    Описание:
        Владелец может "спрашивать" своего питомца и получать ответы."""
    
    def __init__(self, name: str, pet: Kitten) -> None:
        """Инициализирует экземпляр класса Owner.
        
        Параметры:
            name (str): Имя владельца.
            pet (Kitten): Экземпляр котенка."""
        self.name = name
        self.pet = pet  # Композиция: объект Kitten является частью объекта Owner
    
    def ask_pet(self) -> str:
        """"Спрашивает" питомца и возвращает его ответ.
        
        Результат:
            str: Ответ питомца."""
        return self.pet.to_answer()


# Пример использования
if __name__ == "__main__":
    kitten = Kitten("Whiskers")
    owner = Owner("Alice", kitten)
    
    # Демонстрация полиморфизма (если бы были другие классы-наследники Animal)
    animals: list[Animal] = [kitten]  # Можно добавить другие классы, реализующие Animal
    
    for animal in animals:
        print(animal.to_answer())  # moore-moore
        print(animal.to_answer())  # meow-meow
    
    print(f"Ответы 'да': {kitten.number_yes()}")  # 2
    print(f"Ответы 'нет': {kitten.number_no()}")  # 1
    