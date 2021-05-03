# Функция расчета месячного пплатежа по кредиту
# s - сумма займа
# r - годовая процентная ставка от 0 до 1
# n - срок кредита в месяцах
# Пример использования: calculate_credit(20000, 0.12, 36) вернет 664
def calculate_credit(s, r, n):
    if (0 < r <= 1) and (type(s) == int and type(n) == int):
        r = r / 12
        result = int(s * (r * (1 + r) ** n) / ((1 + r) ** n - 1))
        return result
    else:
        return 'Вы ввели недопустимое значение'


# Простой класс калькулятора
class Calculator():

    # метод сложения чисел
    def sum(self, a, b):
        return a + b

    # метод умножения чисел
    def mult(self, a, b):
        return a * b
