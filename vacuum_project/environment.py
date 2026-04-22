import numpy as np
import random

class VacuumEnvironment:
    def __init__(self, width=4, height=4, dirt_probability=0.3):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int) # 0 is clean, 1 is dirty
        self.dirt_probability = dirt_probability
        self._initialize_dirt()

    def _initialize_dirt(self):
        """scatter dirt around based on the probability"""
        for y in range(self.height):
            for x in range(self.width):
                if random.random() < self.dirt_probability:
                    self.grid[y][x] = 1

    def is_dirty(self, x, y):
        return self.grid[y][x] == 1

    def clean_square(self, x, y):
        self.grid[y][x] = 0

    def is_goal_reached(self):
        """check if the whole grid is clean"""
        return np.sum(self.grid) == 0

    def get_percept(self, x, y):
        """what the agent sees right now"""
        return ((x, y), self.is_dirty(x, y))