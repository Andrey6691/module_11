import matplotlib.pyplot as plt
import pandas as pd
import requests

"""Requests — это модуль для языка Python, который используют для упрощения работы с HTTP-запросами."""

print("\nКод requests\n")

response = requests.get('https://api.github.com')
print(response.json())


print("\nКод Matplotlib\n")

"""Matplotlib — это библиотека для визуализации данных в Python. Она используется для создания любых видов графиков: 
линейных, круговых диаграмм, построчных гистограмм и других — в зависимости от задач"""

x = [1, 2, 3, 4, 5]
y = [2, 5, 3, 7, 3]

plt.plot(x, y, color='red', marker='o', markersize=10)

plt.title('график')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

plt.show()

"""Библиотека pandas применяется для обработки и анализа табличных данных."""

print("\nКод Pandas\n")

Data = [1, 2, 3, 4, 5, 6, 7]
s = pd.Series(Data)
Index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
si = pd.Series(Data, Index)
print(si)


