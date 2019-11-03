from enum import Enum


class Side(Enum):
    LEFT = 1
    RIGHT = 2
    TOP = 3
    BOTTOM = 4

    def is_vertical(self):
        return self.value >= 3
