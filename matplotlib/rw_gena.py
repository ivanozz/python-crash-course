"""
генерируем случайное блуждание по кварталам
"""
import matplotlib.pyplot as plt

from random_gena import RandomGena

# построение случайного блуждания и нанесение точек на диаграмму
#while True:
plt.figure(dpi=128, figsize=(10, 6))

plt.scatter(0, 0, c='green', edgecolor='none', s=100)
for i in range(1, 200):
    rw = RandomWalk(50)
    rw.fill_walk()

    points_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values, c="gray", marker="v")

    # нанесение крайних точек блуждания
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)
    plt.pause(1)

#plt.axis([-5, 5, -5, 5])
# удаление осей
#plt.axes().get_xaxis().set_visible(False)
#plt.axes().get_yaxis().set_visible(False)

plt.show()
