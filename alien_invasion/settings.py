class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициирует настройки игры"""

        # параметры экрана
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # количество жизней
        self.ship_limit = 3

        # параметры пули
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # настройка пришельцев
        self.fleet_drop_speed = 10
        # темп ускорения игры
        self.speedup_scale = 1.1
        # темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # величина смещения корабля при каждой итерации
        self.ship_speed_factor = 1.5
        # скорость пули
        self.bullet_speed_factor = 5
        # скорость пришельца
        self.alien_speed_factor = 1
        # fleet_direction = 1 - движение вправо, -1 - влево
        self.fleet_direction = 1
        # подсчет очков
        self.alien_points = 50
        # todo: реализовать вывод точности игрока (отношения попаданий к общему числу выстрелов)

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
