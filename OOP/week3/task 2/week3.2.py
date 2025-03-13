from abc import ABC, abstractmethod
from typing import List, Dict

class Pizza(ABC):
    """
    Абстрактный базовый класс для пиццы.
    Описание: Этот класс определяет общий интерфейс для всех видов пицц.
    """

    def __init__(self, name: str, dough: str, sauce: str, toppings: List[str]):
        """
        Инициализация экземпляра класса Pizza.
        Параметры:
        - name: название пиццы.
        - dough: тип теста.
        - sauce: тип соуса.
        - toppings: список начинок.
        """
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

    @abstractmethod
    def prepare(self) -> None:
        """
        Подготовка пиццы: замес теста, добавление соуса и начинок.
        Результат: None.
        """
        pass

    def bake(self) -> None:
        """
        Выпечка пиццы.
        Результат: None.
        """
        print("Выпекаем пиццу...")

    def cut(self) -> None:
        """
        Нарезка пиццы.
        Результат: None.
        """
        print("Нарезаем пиццу...")

    def pack(self) -> None:
        """
        Упаковка пиццы.
        Результат: None.
        """
        print("Упаковываем пиццу...")

    def __call__(self) -> None:
        """
        Вызываемый метод для приготовления пиццы.
        Результат: None.
        """
        self.prepare()
        self.bake()
        self.cut()
        self.pack()

    def __str__(self) -> str:
        """
        Возвращает строковое представление пиццы.
        Результат: строка.
        """
        return f"{self.name} (тесто: {self.dough}, соус: {self.sauce}, начинки: {', '.join(self.toppings)})"


class PepperoniPizza(Pizza):
    """
    Класс для пиццы Пепперони.
    Описание: Этот класс реализует конкретный вид пиццы.
    """

    def __init__(self):
        super().__init__(
            name="Пепперони",
            dough="тонкое",
            sauce="томатный",
            toppings=["пепперони", "сыр моцарелла"]
        )

    def prepare(self) -> None:
        print(f"Готовим пиццу {self.name}:")
        print(f" - Замешиваем {self.dough} тесто.")
        print(f" - Добавляем {self.sauce} соус.")
        print(f" - Добавляем начинки: {', '.join(self.toppings)}.")


class BarbecuePizza(Pizza):
    """
    Класс для пиццы Барбекю.
    Описание: Этот класс реализует конкретный вид пиццы.
    """

    def __init__(self):
        super().__init__(
            name="Барбекю",
            dough="толстое",
            sauce="барбекю",
            toppings=["курица", "лук", "сыр моцарелла"]
        )

    def prepare(self) -> None:
        print(f"Готовим пиццу {self.name}:")
        print(f" - Замешиваем {self.dough} тесто.")
        print(f" - Добавляем {self.sauce} соус.")
        print(f" - Добавляем начинки: {', '.join(self.toppings)}.")


class SeafoodPizza(Pizza):
    """
    Класс для пиццы Дары Моря.
    Описание: Этот класс реализует конкретный вид пиццы.
    """

    def __init__(self):
        super().__init__(
            name="Дары Моря",
            dough="тонкое",
            sauce="сливочный",
            toppings=["креветки", "мидии", "сыр моцарелла"]
        )

    def prepare(self) -> None:
        print(f"Готовим пиццу {self.name}:")
        print(f" - Замешиваем {self.dough} тесто.")
        print(f" - Добавляем {self.sauce} соус.")
        print(f" - Добавляем начинки: {', '.join(self.toppings)}.")


class Order:
    """
    Класс для заказа.
    Описание: Этот класс содержит список заказанных пицц и умеет подсчитывать стоимость заказа.
    """

    def __init__(self):
        self.pizzas: List[Pizza] = []

    def add_pizza(self, pizza: Pizza) -> None:
        """
        Добавляет пиццу в заказ.
        Параметры:
        - pizza: экземпляр класса Pizza.
        Результат: None.
        """
        self.pizzas.append(pizza)

    def calculate_total(self) -> float:
        """
        Подсчитывает общую стоимость заказа.
        Результат: стоимость заказа (float).
        """
        return len(self.pizzas) * 10.0  # Упрощенная логика расчета стоимости

    def __str__(self) -> str:
        """
        Возвращает строковое представление заказа.
        Результат: строка.
        """
        return "\n".join(str(pizza) for pizza in self.pizzas)


class Terminal:
    """
    Класс для терминала.
    Описание: Этот класс отвечает за взаимодействие с пользователем.
    """

    def __init__(self):
        self.menu: Dict[int, Pizza] = {
            1: PepperoniPizza(),
            2: BarbecuePizza(),
            3: SeafoodPizza()
        }
        self.order: Order = Order()

    def display_menu(self) -> None:
        """
        Отображает меню пицц.
        Результат: None.
        """
        print("Меню:")
        for key, pizza in self.menu.items():
            print(f"{key}. {pizza.name}")

    def take_order(self) -> None:
        """
        Принимает заказ от пользователя.
        Результат: None.
        """
        while True:
            self.display_menu()
            choice = input("Выберите номер пиццы (или 'готово' для завершения): ")
            if choice.lower() == "готово":
                break
            try:
                pizza = self.menu[int(choice)]
                self.order.add_pizza(pizza)
                print(f"Добавлено: {pizza.name}")
            except (KeyError, ValueError):
                print("Неверный выбор. Попробуйте снова.")

    def confirm_order(self) -> None:
        """
        Подтверждает заказ и выставляет счет.
        Результат: None.
        """
        print("\nВаш заказ:")
        print(self.order)
        print(f"Итого к оплате: ${self.order.calculate_total():.2f}")
        payment = input("Введите сумму оплаты: ")
        try:
            if float(payment) >= self.order.calculate_total():
                print("Оплата принята. Ваш заказ готовится.")
                for pizza in self.order.pizzas:
                    pizza()  # Готовим пиццу
            else:
                print("Недостаточно средств. Заказ отменен.")
        except ValueError:
            print("Неверная сумма. Заказ отменен.")


# Пример использования
if __name__ == "__main__":
    terminal = Terminal()
    terminal.take_order()
    terminal.confirm_order()