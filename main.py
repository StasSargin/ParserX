import requests
from bs4 import BeautifulSoup
# import csv
# import re


# Функция получения html.
def get_html(url):
    request = requests.get(url)
    if request.ok:                  # Сервер вернул код 200.
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


# # Форматируем полученную строку.
# def refined(string):
#     result = string.split(' ')[1]
#     return result


# Функция получения данных.
def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')  # Вторым атрибутом указываем нужный парсер.
    items = soup.find_all('div', class_="model")
    for item in items:
        try:
            name = item.find_all('a')[0].text.strip()
        except:
            name = ''                   # Если значения нет, то записываем пустую строку.

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


    # for page_number in range(0, 5):   # Пагинатор по количеству страниц.
    #     get_page_data(get_html(url + str(page_number)))


    # while True:                       # Пагинатор по кнопке Next.
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
