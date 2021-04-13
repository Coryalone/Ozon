# -*- coding: utf-8 -*-
import csv
import re
from bs4 import BeautifulSoup
import requests


# задание 1

with open("lesson09_closest_galaxies.csv", encoding="utf8") as f:
    reader = csv.DictReader(f, delimiter = ',')
    for row in reader:
        galaxi = re.sub(r'\[\w+]', '', row['Галактика'])
        galaxi = re.sub(r'\(', '', galaxi)
        galaxi = re.sub(r'\)', '', galaxi)
        galaxi = re.sub(r'англ.', '', galaxi)
        if (re.search('Рыбы', galaxi) or re.search('Пегас', galaxi) or re.search('Кит', galaxi)) \
        or re.search(r'^[A-Za-z]', galaxi) or re.search(r'[0-9]$', galaxi):
            print(galaxi) 
print()

# задание 2

list_of_closest_galaxies = []
with open("lesson09_closest_galaxies.csv", encoding="utf8") as f:
    reader = csv.DictReader(f, delimiter = ',')
    for row in reader:
        distance = re.sub(r'\[\w+]', '', row['Расстояние от Земли млн св. лет'])
        distance = re.sub(r'[\?]+', '', distance) 
        distance = re.sub(r'\—', '', distance)
        galaxi = re.sub(r'\[\w+]', '', row['Галактика'])
        if (re.search('Андромед', galaxi) or re.search('Андромед', row['Примечания'])  ) and distance != '':
            list_of_closest_galaxies.append({'Название': galaxi, 'Расстояние': float(distance), 'Примечания': row['Примечания']})
        
list_of_closest_galaxies = sorted(list_of_closest_galaxies, key=lambda x: x['Расстояние'])
print(list_of_closest_galaxies)
print()

# задание 3

with open('lesson09_cats_of_ulthar.txt', 'r') as f:
    reader = f.read()
count_of_cats = re.findall(r'(кошек|кошк)', reader, flags = re.IGNORECASE|re.MULTILINE)
print('Слово \'кошка\' в любом виде встречается ' + str(len(count_of_cats)) + ' раз')
print()

# задание 4

data = requests.get('https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B1%D1%8C%D1%8E%D0%BB%D0%B0')
data = data.text
soup = BeautifulSoup(data, 'html.parser')

links =  soup.find_all('a')
for link in links:
    if  link.has_attr('href'):
        if re.search(r'.+(?=:)', link['href']) and not 'wiki' in link['href'] and not '#' in link['href'] and not re.search(r'^\/w/index\.php', link['href']):
            print(link['href'])