from deposit import TermDeposit, BonusDeposit, CompoundDeposit, DepositRecommender

def main():
    # Создаем рекомендатель вкладов
    recommender = DepositRecommender()
    
    # Добавляем дополнительный вклад
    recommender.add_deposit(
        BonusDeposit("Супербонус", 200_000, 0.08, 24, 500_000, 0.3)
    )
    
    # Примеры использования
    print("Пример 1: Вклад 150 000 ₽ на 12 месяцев")
    recommender(150_000, 12)
    
    print("\nПример 2: Вклад 75 000 ₽ на 24 месяца")
    recommender(75_000, 24)
    
    print("\nПример 3: Вклад 5 000 ₽ на 12 месяцев (недостаточная сумма)")
    recommender(5_000, 12)

if __name__ == "__main__":
    main()