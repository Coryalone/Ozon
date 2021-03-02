def age_in_future():
    birth_date = int(input('В каком году вы родились?: '))
    future_year = int(input('К какому году нужно посчитать возраст?: '))
    age_in_time = future_year - birth_date

    if str(age_in_time).endswith('11'):
        print('Ваш возраст в будущем',age_in_time,'лет')
    elif str(age_in_time).endswith('12'):
        print('Ваш возраст в будущем',age_in_time,'лет')
    elif str(age_in_time).endswith('13'):
        print('Ваш возраст в будущем',age_in_time,'лет')
    elif str(age_in_time).endswith('14'):
        print('Ваш возраст в будущем',age_in_time,'лет')
    elif str(age_in_time).endswith('15'):
        print('Ваш возраст в будущем',age_in_time,'лет')
    elif str(age_in_time).endswith('16'):
        print('Ваш возраст в будущем',age_in_time,'лет')
    elif str(age_in_time).endswith('17'):
        print('Ваш возраст в будущем',age_in_time,'лет')
    elif str(age_in_time).endswith('18'):
        print('Ваш возраст в будущем',age_in_time,'лет')
    elif str(age_in_time).endswith('19'):
        print('Ваш возраст в будущем',age_in_time,'лет')                                
    elif str(age_in_time).endswith('1'):
        print('Ваш возраст в будущем',age_in_time,'год')
    elif str(age_in_time).endswith('2'): 
        print('Ваш возраст в будущем',age_in_time,'года')
    elif str(age_in_time).endswith('3'):
        print('Ваш возраст в будущем',age_in_time,'года')
    elif str(age_in_time).endswith('4'):
        print('Ваш возраст в будущем',age_in_time,'года')
    else:
        print('Ваш возраст в будущем',age_in_time,'лет')


def average_salary():
    first_person = int(input('Какая у вас зарплата?: '))
    second_person = int(input('Какая у вас зарплата?: '))
    third_person = int(input('Какая у вас зарплата?: '))

    print('Каждый член семьи может потратить: ', round((first_person + second_person + third_person) / 3))

            