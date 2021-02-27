from decimal import Decimal

def age_in_future():
    q=int(input('В каком году вы родились?: '))
    w=int(input('К какому году нужно посчитать возраст?: '))
    age_in_time=w-q

    print('Ваш возраст в будущем',age_in_time, "годов")
  


def average_salary():
    q=int(input('Какая у вас зарплата?: '))
    w=int(input('Какая у вас зарплата?: '))
    e=int(input('Какая у вас зарплата?: '))

    print('Каждый член семьи может потратить: ', round(q+w+e)/3)

   
