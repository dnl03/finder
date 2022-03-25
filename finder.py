from bs4 import BeautifulSoup
from requests import get
from notify_run import Notify
import time

notify=Notify()

while True:
    lokal = time.localtime()
    czas = lokal.tm_hour * 60 + lokal.tm_min
    URL = 'https://www.olx.pl/motoryzacja/samochody/skoda/fabia/zawoja/?search%5Bfilter_float_price%3Ato%5D=6000&search%5Bfilter_float_enginesize%3Afrom%5D=1250&search%5Bfilter_enum_petrol%5D%5B0%5D=petrol&search%5Bfilter_enum_petrol%5D%5B1%5D=lpg&search%5Bfilter_float_milage%3Ato%5D=190000&search%5Bdist%5D=100'
    page = get(URL)
    bs = BeautifulSoup(page._content, 'html.parser')
    for offer in bs.find_all('div', class_='offer-wrapper'):
        name = offer.find('h3', class_='lheight22 margintop5').get_text().strip()
        footer = offer.find('td', class_='bottom-cell')
        date = footer.find_all('small', class_='breadcrumb x-normal')[1].get_text().strip()
        link = offer.find('a')
        if date.split(' ')[0] == "dzisiaj" and (czas-(int(date.split(' ')[1].split(':')[0])*60+int(date.split(' ')[1].split(':')[1])))<10:
            notify.send(date+":"+name, link['href'])
    time.sleep(120)