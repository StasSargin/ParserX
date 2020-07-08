import requests
from bs4 import BeautifulSoup
import csv


# Функция получения html.
def get_html(url):
    request = requests.get(url)
    if request.ok:              # Сервер вернул код 200.
        return request.text
    print(request.status_code)  # Выводим код ошибки.


# # Функция записи в csv.
# def write_csv(data):
#     with open('file.csv', 'a') as file:
#         writer = csv.writer(file)
#
#         writer.writerow([
#             data['name'],
#             data['link'],
#             ])


# # Форматируем полученную строку.
# def refined(string):
#     result = string.split(' ')[1]
#     return result


# Функция получения данных.
def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')  # Вторым атрибутом указываем нужный парсер.
    items = soup.find_all('div', class_="model")
    for item in items:
        try:                            # Если значения нет, то записываем пустую строку.
            name = item.find_all('a')[0].text
        except:
            name = ''
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

    # for page_number in range(0, 5):  # Пагинатор по количеству страниц.
    #     get_page_data(get_html(url + str(page_number)))


if __name__ == '__main__':
    main()