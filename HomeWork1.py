import matplotlib.pyplot as plt
import numpy as np

# Параметры нормального распределения
mean = 0 # Среднее значение
std_dev = 1 # Стандартное отклонение
num_samples = 1000 # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.hist(data, bins=20)
plt.title('Нормальное распределение')
plt.xlabel('Значение образцов')
plt.ylabel('Количество образцов')
plt.show()

# Генерация двух наборов случайных чисел
random_array_x = np.random.rand(5)
random_array_y = np.random.rand(5)

# Построение диаграммы рассеяния
plt.scatter(random_array_x, random_array_y)
plt.title('Диаграмма рассеяния')
plt.xlabel('ось х')
plt.ylabel('ось у')
plt.show()