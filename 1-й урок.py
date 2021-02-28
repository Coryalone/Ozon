def age_in_future():
    birth_date = int(input('В каком году вы родились?: '))
    future_year = int(input('К какому году нужно посчитать возраст?: '))
    age_in_time = future_year - birth_date

    if age_in_time % 10 == 1:
        print('Ваш возраст в будущем', age_in_time, 'год')
    elif age_in_time % 10 == 2: 
        print('Ваш возраст в будущем', age_in_time, 'года')
    elif age_in_time % 10 == 3:
        print('Ваш возраст в будущем', age_in_time, 'года')
    elif age_in_time % 10 == 4:
        print('Ваш возраст в будущем', age_in_time, 'года')
    else:
        print('Ваш возраст в будущем', age_in_time, 'лет')
  

def average_salary():
    first_person = int(input('Какая у вас зарплата?: '))
    second_person = int(input('Какая у вас зарплата?: '))
    third_person = int(input('Какая у вас зарплата?: '))

    print('Каждый член семьи может потратить: ', round((first_person + second_person + third_person) / 3))


  
