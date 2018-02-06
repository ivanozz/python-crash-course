from random import choice

class RandomWalk():
    """Класс для генерирования случайных блужданий"""

    def __init__(self, num_points=5000):
        """Инициирует атрибуты блуждания"""

        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Вычисляет все точки блуждания"""

        # Шаги генерируются до достижения нужной длины
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, 0, -1])
            x_distance = choice([0, 1])
            x_step = x_direction * x_distance

            if x_direction == 0:
                x_distance = 1
            else:
                x_distance = choice([0, 1])

            if x_direction == 0 :
                y_direction = choice([1, -1])
            else :
                y_direction = 0

            if y_direction == 0:
                y_distance = 1
            else:
                y_distance = choice([0, 1])

            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            # вычисление следующих значений
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

