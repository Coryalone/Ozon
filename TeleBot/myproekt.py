import random
import telebot
import requests
from bs4 import BeautifulSoup as BS
from telebot import types
import re
import datetime
import time


bot = telebot.TeleBot("1777037080:AAGHut45GniubiW4f5ejHqbD0RYeMz1We2w")

data = requests.get('https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8')
data = data.text
soup = BS(data, 'html.parser')

list_of_Russia_city = []
links = soup.find_all('tr')
for link in links:
    link = (link.find('td', {'align': 'left'}))
    if link != None and link.has_attr('align'):
        list_of_Russia_city.append(link.find('a').text)

def pars_weather(city):
    date = datetime.datetime.today()
    date = datetime.datetime.date(date)    
    tomorrow = datetime.datetime.today()
    tomorrow = tomorrow + datetime.timedelta(days=1)
    tomorrow = datetime.datetime.date(tomorrow)    
    if re.search(r'\/', city):
        current_date = re.sub(r'[а-я-А-Я]+\/', '', city)
        current_date = current_date.replace('-', '')
        current_date = datetime.datetime.strptime(current_date, '%Y%m%d').date()
        if current_date > date and current_date == tomorrow:
            r = requests.get(f'https://sinoptik.ua/погода-{city}')
            html = BS(r.content, 'html.parser')
            for el in html.select('#content'):
                zavtra = 'Завтра ' + el.select('.temperature .min')[1].text, el.select('.temperature .max')[1].text
                text = el.select('.wDescription .description')[0].text
                return f'{str(zavtra[0])} {str(zavtra[1])}. {text}'
        elif current_date > tomorrow:
            r = requests.get(f'https://sinoptik.ua/погода-{city}')
            html = BS(r.content, 'html.parser')
            for el in html.select('#content'):
                poslezavtra = 'Послезавтра ' + el.select('.temperature .min')[2].text, el.select('.temperature .max')[2].text
                text = el.select('.wDescription .description')[0].text
                return f'{str(poslezavtra[0])} {str(poslezavtra[1])}. {text}'
        else:
            pass
    else:
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
    intro = random.choice(['Гугл говорит: ', 'Давай глянем! ', 'Отличный Вопрос! ', 'Мне тоже интересно! '])
    city = message.text
    if city == '/start':
        pass
    else:
        city = city.title().strip()
    if re.search(r'[а-я-А-Я]+\s[скоро]+', message.text):
        if re.search(r'\s[скоро]+', message.text).group(0).strip().lower() == 'скоро'.lower() and re.search(r'[а-я-А-Я]+', message.text).group(0).strip() in list_of_Russia_city:
            city = re.sub(r'\s[а-я-А-Я]+', '', message.text)
            city = city.title().strip()
            date = datetime.datetime.today()
            date = datetime.datetime.date(date)
            tomorrow = datetime.datetime.today()
            tomorrow = tomorrow + datetime.timedelta(days=1)
            tomorrow = tomorrow.strftime("%Y-%m-%d")
            tomorrow = city + '/' + tomorrow            
            day_after_tomorrow = datetime.datetime.today()
            day_after_tomorrow = day_after_tomorrow + datetime.timedelta(days=2)
            day_after_tomorrow = day_after_tomorrow.strftime("%Y-%m-%d")
            day_after_tomorrow = city + '/' + day_after_tomorrow            
            bot.send_message(message.chat.id, f'{intro}{message.from_user.first_name}, погода в городе {city} на ближайшие дни:\n \n' + f'Сегодня: ' + str(pars_weather(city)) +'\n' \
                             + '\n' + str(pars_weather(tomorrow)) + '\n' +'\n' + str(pars_weather(day_after_tomorrow)))
        else:
            bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}. Если хочешь узнать погоду на несколько дней, напиши название города, поставь пробел и добавь слово "скоро"')
    else:
        if city in list_of_Russia_city:
            bot.send_message(message.chat.id, f'{intro}{message.from_user.first_name}, погода в городе {city} сегодня:\n' + str(pars_weather(city)))
        elif city == '/start':
            bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}. Я - Бот, который показывает погоду в городах России.\n Если хочешь узнать погоду на несколько дней, напиши название города, поставь пробел и добавь слово "скоро".\n Если хочешь узнать погоду только на сегодня, напиши только название города. Погода в каком городе России интересует тебя?')
        elif re.search(r'[а-я-А-Я]+\s\/[a-z]+', city):
            pass
        else:
            bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}. В России нет такого города, введи, пожалуйста, корректное название города')
        
bot.polling()