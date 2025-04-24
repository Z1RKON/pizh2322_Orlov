from date import Date
from datetime import timedelta

def test_date_class():
    print("=== Тестирование класса Date ===")
    
    # Создание объектов
    date1 = Date(2023, 5, 15)
    date2 = Date.from_string("2023-05-20")
    
    print(f"Дата 1: {date1}")
    print(f"Дата 2: {date2}")
    
    # Вызываемый метод
    print(f"Дата 1 как словарь: {date1()}")
    
    # Свойства
    print(f"Год: {date1.year}, Месяц: {date1.month}, День: {date1.day}")
    
    # Методы
    print(f"День недели: {date1.day_of_week()}")
    print(f"Это выходной? {'Да' if date1.is_weekend() else 'Нет'}")
    print(f"Дней между датами: {date1.days_until(date2)}")
    
    # Арифметические операции
    date3 = date1 + 5
    print(f"Дата1 + 5 дней: {date3}")
    
    date4 = date2 - timedelta(days=3)
    print(f"Дата2 - 3 дня: {date4}")
    
    diff = date2 - date1
    print(f"Разница между датами: {diff} дней")
    
    # Сравнения
    print(f"Дата1 == Дата2? {'Да' if date1 == date2 else 'Нет'}")
    print(f"Дата1 < Дата2? {'Да' if date1 < date2 else 'Нет'}")
    
    # Сохранение и загрузка
    filename = "date.json"
    date1.save(filename)
    loaded_date = Date.load(filename)
    print(f"Загруженная дата: {loaded_date}")
    print(f"Совпадает с оригиналом? {'Да' if date1 == loaded_date else 'Нет'}")

if __name__ == "__main__":
    test_date_class()