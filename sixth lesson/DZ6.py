import show_rating as rs #задание 1
import re


shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',\
 'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,\
 'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}

list_of_drama = rs.select_titles(shows, 'драма')            
list_of_crime = rs.select_titles(shows, 'криминал')

print(rs.rate_avg(ratings, list_of_drama))
print(rs.rate_avg(ratings, list_of_crime))
print()

#задание 2

sub_string = 'кошка'
with open('cats.txt') as f:
    lines_of_file = f.readlines()

count_of_cats = 0    

result_of_selection = []
for i in lines_of_file:
    result_of_selection = re.findall(r'\bкошка\b', i)
    for i in range(len(result_of_selection)):
        if result_of_selection[i] == sub_string:
            count_of_cats += 1
print('Слово \'кошка\' встречается ' + str(count_of_cats) + ' раз')
print()

for i in lines_of_file:
    if  re.search(r"\bкошка\b", i):
            print(i)
print()
#задание 3 
  
date = input('Введите текущую дату: ')
event = input('Введите текущее событие: ')
diary = date + '\n' + event + '\n'

with open('diary.txt', 'a') as f:
    f.write(diary)

with open('diary.txt') as f:
    lines = f.readlines()

for i in lines:
    print(i.strip())
print()

#задание 4

filename = 'pi_million_digits.txt'
with open(filename) as file:
    lines = file.readlines()
    
pi_string = ''

for line in lines:
    pi_string += line

birthyear = input('Ведите дату вашего рождения ')
if birthyear in pi_string:
    print('Первое вхождение находится по индексу: ' + str(pi_string.find(birthyear))) 
else:
    print('Такой год остутствует')

    






