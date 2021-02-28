def age_in_future():
    birth_date = int(input('В каком году вы родились?: '))
    future_year = int(input('К какому году нужно посчитать возраст?: '))
    age_in_time = future_year - birth_date

    
    if  len(str(age_in_time))>1 and (str(age_in_time)[-1]=='1' and str(age_in_time)[-2]=='1'):
            print('Ваш возраст в будущем',age_in_time,'лет')
    elif len(str(age_in_time))>1 and (str(age_in_time)[-1]=='2' and str(age_in_time)[-2]=='1'):
            print('Ваш возраст в будущем',age_in_time,'лет')
    elif len(str(age_in_time))>1 and (str(age_in_time)[-1]=='3' and str(age_in_time)[-2]=='1'):
            print('Ваш возраст в будущем',age_in_time,'лет')
    elif len(str(age_in_time))>1 and (str(age_in_time)[-1]=='4' and str(age_in_time)[-2]=='1'):
            print('Ваш возраст в будущем',age_in_time,'лет')
    elif len(str(age_in_time))>1 and (str(age_in_time)[-1]=='5' and str(age_in_time)[-2]=='1'):
            print('Ваш возраст в будущем',age_in_time,'лет')
    elif len(str(age_in_time))>1 and (str(age_in_time)[-1]=='6' and str(age_in_time)[-2]=='1'):
            print('Ваш возраст в будущем',age_in_time,'лет')
    elif len(str(age_in_time))>1 and (str(age_in_time)[-1]=='7' and str(age_in_time)[-2]=='1'):
            print('Ваш возраст в будущем',age_in_time,'лет')
    elif len(str(age_in_time))>1 and (str(age_in_time)[-1]=='8' and str(age_in_time)[-2]=='1'):
            print('Ваш возраст в будущем',age_in_time,'лет')
    elif len(str(age_in_time))>1 and (str(age_in_time)[-1]=='9' and str(age_in_time)[-2]=='1'):
            print('Ваш возраст в будущем',age_in_time,'лет')
    elif str(age_in_time)[-1]=='1':
        print('Ваш возраст в будущем',age_in_time,'год')                                       
    elif str(age_in_time)[-1]=='2':
        print('Ваш возраст в будущем',age_in_time,'года')
    elif str(age_in_time)[-1]=='3': 
        print('Ваш возраст в будущем',age_in_time,'года')
    elif str(age_in_time)[-1]=='4': 
        print('Ваш возраст в будущем',age_in_time,'года')
    else:
        print('Ваш возраст в будущем',age_in_time,'лет')
  

def average_salary():
    first_person = int(input('Какая у вас зарплата?: '))
    second_person = int(input('Какая у вас зарплата?: '))
    third_person = int(input('Какая у вас зарплата?: '))

    print('Каждый член семьи может потратить: ', round((first_person + second_person + third_person) / 3))


  
