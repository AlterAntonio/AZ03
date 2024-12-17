from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import pandas as pd
from matplotlib import pyplot as plt
import os

# Инициализация драйвера
driver = webdriver.Chrome()

# URL страницы "Все диваны"
# url = 'https://www.divan.ru/category/divany'

# Локально сохранённая mhtml-страница
current_dir = os.path.dirname(os.path.abspath(__file__))
url = os.path.join(current_dir, 'Divan.ru.mhtml')

# Открываем выбранный вариант
driver.get(url)
time.sleep(5)

# Парсинг цен с добавлением в список
prices = []
for element in driver.find_elements(By.CSS_SELECTOR, ".ui-LD-ZU.KIkOH"):
    text = element.text.replace('руб.', '').replace(' ', '')
    prices.append(int(text))

# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price])

# Закрытие драйвера
driver.quit()

# Чтение из файла
df = pd.read_csv('prices.csv')

# Выводим среднюю цену
print(f"Среднестатистическая цена дивана: {int(df['Price'].mean())}")

# Рендеринг гистограммы цен
plt.hist(df['Price'], bins=len(df['Price']))
plt.title('Цены на диваны')
plt.xlabel('Цена, руб.')
plt.ylabel('Количество предложений')
plt.show()