from abc import ABC, abstractmethod
from typing import Dict, List, Union

class BankDeposit(ABC):
    """
    Абстрактный базовый класс для банковских вкладов.
    Описание: Определяет общий интерфейс для всех типов вкладов.
    """
    
    def __init__(self, name: str, min_amount: float, rate: float, period: int):
        """
        Инициализация базового класса вклада.
        Параметры:
            name: Название вклада
            min_amount: Минимальная сумма вклада
            rate: Процентная ставка (в долях от 1)
            period: Срок вклада (в месяцах)
        """
        self.name = name
        self.min_amount = min_amount
        self.rate = rate
        self.period = period
    
    @abstractmethod
    def calculate_profit(self, amount: float) -> float:
        """
        Расчет прибыли по вкладу.
        Параметры:
            amount: Сумма вклада
        Результат:
            Размер прибыли
        """
        pass
    
    def __call__(self, amount: float) -> float:
        """
        Вызываемый метод для расчета прибыли.
        Параметры:
            amount: Сумма вклада
        Результат:
            Размер прибыли
        """
        return self.calculate_profit(amount)
    
    def __str__(self) -> str:
        """Строковое представление вклада"""
        return (f"{self.name} (мин. {self.min_amount:.2f} ₽, "
                f"{self.rate*100:.1f}% годовых, срок {self.period} мес.)")

class TermDeposit(BankDeposit):
    """
    Срочный вклад с простыми процентами.
    Описание: Прибыль рассчитывается по формуле простых процентов.
    """
    
    def calculate_profit(self, amount: float) -> float:
        """
        Расчет по формуле: сумма * ставка * период (в годах)
        Параметры:
            amount: Сумма вклада
        Результат:
            Размер прибыли
        """
        if amount < self.min_amount:
            raise ValueError(f"Минимальная сумма вклада {self.min_amount:.2f} ₽")
        return amount * self.rate * (self.period / 12)

class BonusDeposit(BankDeposit):
    """
    Бонусный вклад с дополнительным бонусом.
    Описание: Начисляет бонус к прибыли при выполнении условий.
    """
    
    def __init__(self, name: str, min_amount: float, rate: float, 
                 period: int, bonus_threshold: float, bonus_rate: float):
        """
        Инициализация бонусного вклада.
        Параметры:
            bonus_threshold: Порог для начисления бонуса
            bonus_rate: Процент бонуса от прибыли (в долях от 1)
        """
        super().__init__(name, min_amount, rate, period)
        self.bonus_threshold = bonus_threshold
        self.bonus_rate = bonus_rate
    
    def calculate_profit(self, amount: float) -> float:
        """
        Расчет прибыли с возможным бонусом.
        Параметры:
            amount: Сумма вклада
        Результат:
            Размер прибыли с учетом бонуса
        """
        if amount < self.min_amount:
            raise ValueError(f"Минимальная сумма вклада {self.min_amount:.2f} ₽")
        
        base_profit = amount * self.rate * (self.period / 12)
        
        if amount >= self.bonus_threshold:
            bonus = base_profit * self.bonus_rate
            return base_profit + bonus
        return base_profit

class CompoundDeposit(BankDeposit):
    """
    Вклад с капитализацией процентов.
    Описание: Прибыль рассчитывается с учетом капитализации.
    """
    
    def calculate_profit(self, amount: float) -> float:
        """
        Расчет по формуле сложных процентов.
        Параметры:
            amount: Сумма вклада
        Результат:
            Размер прибыли
        """
        if amount < self.min_amount:
            raise ValueError(f"Минимальная сумма вклада {self.min_amount:.2f} ₽")
        
        monthly_rate = self.rate / 12
        total_amount = amount * (1 + monthly_rate) ** self.period
        return total_amount - amount

class DepositRecommender:
    """
    Класс для подбора оптимального вклада.
    Описание: Осуществляет поиск и сравнение вкладов по параметрам клиента.
    """
    
    def __init__(self):
        """Инициализация с базовым набором вкладов"""
        self.deposits = [
            TermDeposit("Срочный стандарт", 10_000, 0.06, 12),
            BonusDeposit("Бонусный плюс", 50_000, 0.07, 12, 100_000, 0.2),
            CompoundDeposit("Капитализация", 30_000, 0.065, 12)
        ]
    
    def add_deposit(self, deposit: BankDeposit) -> None:
        """
        Добавление нового типа вклада.
        Параметры:
            deposit: Экземпляр класса вклада
        """
        self.deposits.append(deposit)
    
    def recommend(self, amount: float, period: int) -> List[Dict[str, Union[str, float]]]:
        """
        Подбор вкладов по параметрам клиента.
        Параметры:
            amount: Сумма вклада
            period: Желаемый срок (месяцев)
        Результат:
            Список словарей с информацией о подходящих вкладах
        """
        recommendations = []
        
        for deposit in self.deposits:
            if deposit.period == period and amount >= deposit.min_amount:
                try:
                    profit = deposit.calculate_profit(amount)
                    recommendations.append({
                        'deposit': str(deposit),
                        'profit': profit,
                        'total': amount + profit
                    })
                except ValueError:
                    continue
        
        return sorted(recommendations, key=lambda x: x['profit'], reverse=True)
    
    def __call__(self, amount: float, period: int) -> None:
        """
        Вызываемый метод для вывода рекомендаций.
        Параметры:
            amount: Сумма вклада
            period: Желаемый срок (месяцев)
        """
        recs = self.recommend(amount, period)
        
        if not recs:
            print("Нет подходящих вкладов для указанных условий")
            return
        
        print(f"\nРекомендации для суммы {amount:.2f} ₽ на срок {period} мес.:")
        for i, rec in enumerate(recs, 1):
            print(f"{i}. {rec['deposit']}")
            print(f"   Прибыль: {rec['profit']:.2f} ₽")
            print(f"   Итоговая сумма: {rec['total']:.2f} ₽\n")