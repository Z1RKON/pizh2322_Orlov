from date import Date
from dateCollection import DateContainer

def test_date_container():
    print("=== Тестирование DateContainer ===")
    
    # Создаем несколько дат
    date1 = Date(2023, 5, 15)
    date2 = Date.from_string("2023-05-20")
    date3 = Date(2024, 1, 1)
    
    # Создаем контейнер
    container = DateContainer([date1, date2])
    print(container)
    
    # Добавляем дату
    container.add(date3)
    print(f"После добавления: {container}")
    
    # Индексация
    print(f"Первый элемент: {container[0]}")
    
    # Срез
    print(f"Первые два элемента: {container[:2]}")
    
    # Удаление
    removed = container.remove(1)
    print(f"Удален: {removed}, осталось: {container}")
    
    # Вызываемый метод
    print(f"Данные для JSON: {container()}")
    
    # Сохранение и загрузка
    filename = "dates.json"
    container.save(filename)
    
    loaded_container = DateContainer.load(filename)
    print(f"Загруженный контейнер: {loaded_container}")

if __name__ == "__main__":
    test_date_container()