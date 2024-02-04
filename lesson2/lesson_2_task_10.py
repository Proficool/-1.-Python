# X - начальная сумма вклада
# Y - срок вклада в годах
# rate - процентная ставка в год в виде десятичной дроби
# A - конечная сумма на счету

def bank(X, Y):
    rate = 0.1  # 10% годовых
    A = X * (1 + rate) ** Y
    return A

initial_deposit = float(input("Введите начальную сумму вклада: "))
years = int(input("Введите срок вклада в годах: "))

result = bank(initial_deposit, years)
print(f"Сумма на счету спустя {years} лет: {result:.2f} рублей")