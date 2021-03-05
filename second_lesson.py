import random

def virtual_casino():
    acccount = 10000
    print('Вас приветствует программа виртуального казино. Вам предоставляется депозит в 10 000 единиц.Загадайте число, я брошу кубики')

    while acccount != 0:

        guess_number = int(input('выберите любое число...'))
        limit = 12
        random_number = random.randint(0, limit)
        if random_number == guess_number:
            acccount += 12000
            print('Поздравляю, Вам начисленно 12000 единиц.', 'Ваш баланс', acccount, 'единиц')
        else:
            acccount -= 1000
            print('выпало число', random_number, 'Ваш баланс', acccount, 'единиц')
    print('у вас закончились деньги на счету. Приходите завтра')


virtual_casino()