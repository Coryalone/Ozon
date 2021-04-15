import re

shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',\
 'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98, 'Во все тяжкие': 0.85,\
 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}

animals = ['питон', 'питон', 'кит', 'собака', 'питон', 'кит', 'кошка', 'горилла', 'кит', 'кошка', 'жираф', 'леопард', 'жираф',\
 'жираф', 'кошка', 'горилла', 'жираф', 'жираф', 'кошка', 'жираф', 'кошка', 'кошка', 'собака', 'кит',
'жираф', 'леопард', 'жираф', 'собака', 'кит', 'кит', 'кит', 'жираф', 'собака', 'собака', 'кит', 'питон', 'леопард', 'кошка', 'жираф',\
 'собака', 'кошка', 'жираф', 'кошка', 'собака', 'кит', 'леопард', 'леопард', 'горилла',
'горилла', 'кит']

# задание 1

len_of_elenent = list(map(len, animals))
print(len_of_elenent)
print()

len_of_elenent_by_lc = [len(i) for i in animals]
print(len_of_elenent_by_lc)
print()

# задание 2

def func(animal):
    #print(listt)
    if re.search(r'\bк', animal) or re.search(r'\bл', animal):
        return True
    else:
        return False

list_of_filter = list(filter(func, animals))
print(list_of_filter)
print()

list_of_filter_by_lc = [i for i in animals if re.search(r'\bк', i) or re.search(r'\bл', i)]
print(list_of_filter_by_lc)
print()

# задание 3

select_by_genre = {key: value for key, value  in shows.items() if value == 'фэнтази' or value == 'фантастика'} 
print(select_by_genre)
print()

list_of_titles = [key for key in select_by_genre.keys()]
print(list_of_titles)
print()

# задание 4

full_series_info = {key: {'Жанр': value, 'Рейтинг': rate} for key, value in shows.items() for key, rate in ratings.items()}
print(full_series_info)

