import matplotlib.pyplot as plt

from random_walk import RandomWalk

# построение случайного блуждания и нанесение точек на диаграмму
while True:
    rw = RandomWalk(10000)
    rw.fill_walk()
    #plt.figure(figsize=(10,6))
    plt.figure(dpi=128, figsize=(10, 6))

    points_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=points_numbers, cmap=plt.cm.Blues,
        edgecolor='none', s=5)

    #plt.plot(rw.x_values, rw.y_values)
    # нанесение крайних точек блуждания
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
        edgecolor='none', s=100)

    # удаление осей
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
