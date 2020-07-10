import requests
from bs4 import BeautifulSoup


# import csv
# import re


# Функция получения html.
def get_html(url):
    request = requests.get(url)
    if request.ok:  # Сервер вернул код 200.
        return request.text
    else:
        print(request.status_code)  # Выводим код ошибки.


# # Функция записи в csv.
# def write_csv(data):
#     with open('file.csv', 'a') as file:
#         writer = csv.writer(file)
#
#         writer.writerow([
#                          data['name'],
#                          data['link'],
#                          ])

# # Функция №2 записи в csv.
# def write_csv2(data):
#     with open('file.csv', 'a') as file:
#         fieldnames = ['name', 'link']
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#
#         writer.writerow(data)

# # Функция форматирования полученной строки.
# def refined(string):
#     result = string.split(' ')[1]
#     return result

"""
Поиск элементов в BeautifulSoup.
.find() - Найти первый элемент с указанными атрибутами.
.find_all() - Найти все элементы с указанными атрибутами. Получаем список объектов BeautifulSoup.
.parent - Найти родителя элемента.
.find_parent() - Найти родителя элемента с указанными атрибутами.
.find_next_sibling() - Найти следующего брата с указанными атрибутами.
.find_previous_sibling() - Найти предыдущего брата с указанными атрибутами.
"""

"""
Регулярные выражения.
pattern = r'\d' - Найти все цифры в строке.
items = re.findall(pattern, place) - Возвращает список. В атрибутах указываем что и где искать.

pattern = re.compile('\d') - Найти все строки с цифрами.

^ - Начало строки.
$ - Конец строки.
. - Любой символ.
+ - Неограниченное число вхождений.
'\d' - Цифра.
'\w' - Буквы, цифры, _ .
"""


# Функция получения данных.
def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')  # Вторым атрибутом указываем нужный парсер.
    items = soup.find_all('div', class_="model")  # Атрибуты можно записать так: ('div', {'class': model'}).
    for item in items:
        try:
            name = item.find_all('a')[0].text.strip()
        except:
            name = ''  # Если значения нет, то записываем пустую строку.

        try:
            link = 'https://www.yandex.ru' + item.find_all('a')[0].get('href')
        except:
            link = ''

        data = {
            'name': name,
            'link': link
        }

        # write_csv(data)            # Записываем в csv-файл.


# Основная функция.
def main():
    url = "https://www.yandex.ru"
    get_page_data(get_html(url))

    # # Пагинатор по количеству страниц.
    # for page_number in range(0, 5):
    #     get_page_data(get_html(url + str(page_number)))

    # # Пагинатор по кнопке Next.
    # while True:
    #     get_page_data(get_html(url))  # Парсим сначала главную страницу.
    #
    #     soup = BeautifulSoup(get_html(url), 'lxml')
    #     try:                          # Переопределяем url и парсим остальные страницы.
    #         pattern = 'Next'          # Паттерн для регулярного выражения.
    #         next_button_url = "https://www.yandex.ru" + soup.find('a', text=re.compile(pattern)).get('href')
    #     except:                                                      # Ищем url кнопки Next с паттерном.
    #         break


if __name__ == '__main__':
    main()
