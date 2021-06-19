# Данная программа получает список концертов со страницы в ВК
# Импорт модулей
import requests
from bs4 import BeautifulSoup


con = str()
def create_concert():
    concert = []
    url = 'https://vk.com/page-2736916_52464647' # Ссылка на таблицу
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    test = soup.find('table', class_='wk_table').find_all('tr') 
    for i in range(1,len(test)):
        sched = test[i].find_all('td')
        if sched != []:
            when = sched[0].text
            where = sched[1].text
            info = sched[2].find('a').get("href") 
            city = sched[2].find('a').text
            concert.append({
                'Когда':when,
                'Город':where,
                'Ссылка на мероприятие':info,
                'Место' :city
            })
    return concert

