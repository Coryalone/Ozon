import random as rd

shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',\
 'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,\
 'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}



anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма', 'Во все тяжкие': 'криминал', 'Карточный домик': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Игра престолов': 'фэнтази'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

#задание 1

print('Жанр сериала Ведьмак:',shows['Ведьмак'])
print()

a = list(shows.keys())
b = list(shows.values())
print('Названия сериалов:','\n')
for i in a:
    print(i)

print()

print('Названия жанров:','\n')
for i in b:
    print(i)

#задание 2
print()
print('С кем у Ани больше всего общих любимых сериалов?'+'\n')


if len(set(anya.keys()) & set(olya.keys())) > len(set(anya.keys()) & set(nastya.keys())) and \
len(set(anya.keys()) & set(olya.keys())) > len(set(anya.keys()) & set(sveta.keys())):
    print('У Ани больше всего общих любимых сериалов с Олей')
elif len(set(anya.keys()) & set(nastya.keys())) > len(set(anya.keys()) & set(olya.keys())) and \
len(set(anya.keys()) & set(nastya.keys())) > len(set(anya.keys()) & set(sveta.keys())):
    print('У Ани больше всего общих любимых сериалов с Настей')
elif len(set(anya.keys()) & set(sveta.keys())) > len(set(anya.keys()) & set(olya.keys())) and \
len(set(anya.keys()) & set(sveta.keys())) > len(set(anya.keys()) & set(nastya.keys())):
    print('У Ани больше всего общих любимых сериалов со Светой')
else:
    pass       

#задание 3
desired_value = 'фантастика'
  
list_of_keys = []
for key, value in list(shows.items()):
    if value == desired_value:
        a = key.split(' ', 0)
        list_of_keys.append(a)
        
print() 


list_of_ratings = []

for i in range(len(list_of_keys)):
    w = ''.join(list_of_keys[i])
    for key, value in ratings.items():
        if key == w:
            list_of_ratings.append(value)
            avg = (sum(list_of_ratings))/(len(list_of_ratings))

            

print('Средний рейтинг сериалов с жанром "фантастика"=',avg) 

#задание 4
print()

nice_rate = []
godnota = []
hate = 'фэнтази'


for key, value in ratings.items():
    if value >= 0.85:
        nice_rate.append(key)


for key, value in shows.items():
    if  value != hate and key in nice_rate:
        godnota.append(key)


while True:
    throw_dice = rd.choice(list(shows.keys()))
    if throw_dice in godnota:
        recomend = throw_dice
        Vasen =  input(' Мы выбрали для Вас сериал: '+recomend+'\n'+' Желаете посмотреть выбранный для вас сериал? ')
        if Vasen.lower() == 'нет'.lower():
            continue 
        elif Vasen.lower() != 'да'.lower():
            print(' Введите \'Да\' или \'Нет\'')
            continue 
        else:
            print(' Желаем Вам приятного просмотра')
            break    
            


                      