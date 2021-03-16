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
def cross(dictionary, dict2):
    a = set(dictionary.values())
    b = set(dict2.values())
    notnull = a & b
    
    return {'нет общих жанров'}  if notnull == set() else a & b

tuple_of_cross = cross(anya, nastya), cross(olya, sveta), cross(sveta, anya)

print(tuple_of_cross)

#задание 2
print()

def select_titles(dictionary, genre):
    list_of_titles = []   
    for key, value in dictionary.items():
        if value == genre:
            list_of_titles.append(key)
    return  list_of_titles        

list_of_drama = select_titles(shows, 'драма')            
list_of_crime = select_titles(shows, 'криминал')
           

def rate_avg(dictionary, titles):
    list_of_rate = []
     
    for key, value in dictionary.items():
        if key in titles:
            list_of_rate.append(value)
    avg = round((sum(list_of_rate) / len(titles)), 3)
    number_of_serial = len(titles) #задание 3
    return 'Средний рейтинг сериалов: ' + str(avg), 'Число сериалов: ' + str(number_of_serial)

print(rate_avg(ratings, list_of_drama))
print(rate_avg(ratings, list_of_crime))
print()

def stata(genre):
    serial = select_titles(shows, genre)
    avg = rate_avg(ratings, serial)
    tune = ', '.join(serial)
    avg = list(avg)
    avg = ', '.join(avg)
    return 'Выбраный жанр ' + genre,'Результат выборки: ' + tune, avg


def cicle():
    list_of_unique_genre  = []
    for i in shows.values():
        if i not in list_of_unique_genre:
            list_of_unique_genre.append(i)
    
    for i in  list_of_unique_genre:
        print(stata(i))

cicle()          




    








        








