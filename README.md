# AZ03
 Matplotlib
1. Создай гистограмму для случайных данных, сгенерированных с помощью функции `numpy.random.normal`. 

Параметры нормального распределения:
- mean = 0 # Среднее значение
- std_dev = 1 # Стандартное отклонение
- num_samples = 1000 # Количество образцов

Генерация случайных чисел, распределенных по нормальному распределению:
- data = np.random.normal(mean, std_dev, num_samples)

2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.


3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны.

## ДЗ
Первые два задания выполнены в файле `HomeWork1.py`

Задание с парсингом выполнено в файле `HomeWork2.py`. Тут я столкнулся с некоторыми трудностями, по этому сохранил страницу https://www.divan.ru/category/divany в файл `Divan.ru.mhtml`, и задание выполняется по нему. На всякий случай оставил закомментированную строку с URL.