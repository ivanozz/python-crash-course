class GameStats():
    """Отслеживание статистики для игры Alien Invasion"""

    def __init__(self, ai_settings):
        """Иницирализирует статистику"""
        self.ai_settings = ai_settings
        # рекорд игры
        self.high_score = 0
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Инициализирует статистику, изменяююся в ходе игры"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
