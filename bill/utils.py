import requests
from bs4 import BeautifulSoup
from decimal import Decimal


def get_usd():
    url = 'https://www.nbkr.kg/index.jsp?lang=RUS'
    headers = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find('div', id='stickers').find('div', id='stickers-slider').find('div', id='sticker-exrates').find(
        'div', class_='sticker-body').find('tbody')
    info_usd = pages.find('tr').find('td', class_='exrate').text
    usd = Decimal(info_usd)
    return usd


def get_eu():
    url = 'https://www.nbkr.kg/index.jsp?lang=RUS'
    headers = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find('div', id='stickers').find('div', id='stickers-slider').find('div', id='sticker-exrates').find(
        'div', class_='sticker-body').find('tbody')
    info_eu = list(pages.find_all('tr'))
    eu = Decimal(info_eu[1].find('td', class_='exrate').text)
    return eu


# конвертация в доллар
def conversion_to_usd(usd, eur, kgs):
    USD = Decimal(usd)
    EUR = Decimal((eur * get_eu()) / get_usd())
    KGS = Decimal(kgs / get_usd())
    total = USD + EUR + KGS
    return total


def get_total(instance):
    total = conversion_to_usd(instance.usd, instance.eur, instance.kgs)
    return total


def save_data(student, usd, eur, kgs, penalty_days, penalty_total):
    total = conversion_to_usd(usd, eur, kgs)
    student.penalty_days += penalty_days
    student.penalty_total += penalty_total
    student.total_paid += total
    if total > student.payment_month:
        student.reserve = total - student.payment_month
        student.payment_month = 0
    else:
        student.payment_month = student.payment_month - total - student.reserve
        student.reserve = 0
    student.credit_balance = student.course_price - student.total_paid
    student.save()





