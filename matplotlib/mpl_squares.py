import matplotlib.pyplot as plt

input_values = [x for x in range(1, 11)]
squares = [x**2 for x in range(1, 11)]

plt.plot(input_values, squares, linewidth=5)

# Заголовок диаграммы и меток осей
plt.title("Square Numbers", fontsize=26)
plt.xlabel("Value", fontsize=16)
plt.ylabel("Square of Value", fontsize=16)
plt.tick_params(axis='both', labelsize=14)

plt.show()
