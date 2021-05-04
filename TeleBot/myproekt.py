import random
import telebot
import requests
from bs4 import BeautifulSoup as BS


bot = telebot.TeleBot("1777037080:AAGHut45GniubiW4f5ejHqbD0RYeMz1We2w")

data = requests.get('https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8')
data = data.text
soup = BS(data, 'html.parser')

list_of_Russia_city = []
links = soup.find_all('tr')
for link in links:
    link = (link.find('td', {'align':'left'}))
    if link != None and link.has_attr('align'):
        list_of_Russia_city.append(link.find('a').text)

def pars_weather(city):
    r = requests.get(f'https://sinoptik.ua/погода-{city}')
    html = BS(r.content, 'html.parser')
    for el in html.select('#content'):
        tem_min = el.select('.temperature .min')[0].text
        tem_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text
        return f'{tem_min}, {tem_max}.{text}'

@bot.message_handler(content_types = ['text'])
def send_welcome(message):
    global list_of_Russia_city
    intro = random.choice(['Привет, ', 'Добрый день! ', 'Отличный Вопрос! '])
    city = message.text
    if city == '/start':
        pass
    else:
        city = city.title().strip()
    if city in list_of_Russia_city:
        bot.send_message(message.chat.id, f'{intro}{message.from_user.first_name}, погода в городе {city} сегодня:\n' + str(pars_weather(city)))
    elif city == '/start':
        bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}. Я Бот который показывает погоду в городах России. Для моей корректной работы напиши, пожалуйста, название города России')
    else:
        bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}. В России нет такого города, введи, пожалуйста, корректное название города')
        
bot.polling()