from bs4 import BeautifulSoup
import requests
import re


#задание 1

data = requests.get('https://store.steampowered.com/genre/Free%20to%20Play/')
data = data.text
soup = BeautifulSoup(data, 'html.parser')

game_and_url = {}
links =  soup.find_all('a', class_ = 'tab_item')
for link in links:
    if re.search('Free To Play', link.text):
        text = link.find('div', class_ = 'tab_item_name').text
        anchor = link['href']
        slovar = dict.fromkeys([text], anchor)
        game_and_url.update(slovar)
print(game_and_url)
print()

#задание 2

tag_and_count = {}
tags = soup.find_all('div', class_ = 'tag_count_button')
for tag in tags:
    count_of_game = int(tag.find('span', class_ = 'tag_count tab_filter_control_count').text.replace(',', ''))
    slovar = dict.fromkeys([tag.find('span', class_ = 'tag_name').text], count_of_game)
    tag_and_count.update(slovar)
print(tag_and_count) 
print() 

#задание 3

game_and_tags = {}
tabs =  soup.find_all('div', class_ = 'tab_item_content')
for tab in tabs:
    tag_of_games = tab.find('div', class_ = 'tab_item_top_tags').text.split(',')
    slovar = dict.fromkeys([tab.find('div',  class_ = 'tab_item_name').text], tag_of_games)
    game_and_tags.update(slovar)
print(game_and_tags) 