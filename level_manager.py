from level import Level

class LevelManager:
    def __init__(self, space):
        self.space = space
        self.levels = []
        self.current_level_index = 0
        self.create_levels()

    def create_levels(self):
        # Create multiple levels with increasing difficulty
        level1 = Level(self.space)
        level1.setup_level([(100, 100), (300, 300, 200, 20), (500, 400, 200, 20), (700, 550)])
        
        level2 = Level(self.space)
        level2.setup_level([(100, 100), (300, 200, 200, 20), (500, 300, 200, 20), (300, 400, 200, 20), (700, 550)])
        
        self.levels = [level1, level2]

    def get_current_level(self):
        return self.levels[self.current_level_index]

    def next_level(self):
        if self.current_level_index < len(self.levels) - 1:
            self.current_level_index += 1
            return True
        return False

    def reset_current_level(self):
        self.levels[self.current_level_index] = Level(self.space)
        self.levels[self.current_level_index].setup_level(self.levels[self.current_level_index].level_data)
