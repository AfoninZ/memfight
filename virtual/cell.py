from enum import Enum


class CellFlags(Enum):
    EMPTY = 0
    DAMAGED = 1
    ORIGINAL = 2
    MODIFIED = 3


class Cell:
    def __init__(self, flag, color, value):
        self.flag = flag
        self.color = color
        self.value = value

    def set_flag(self, flag):
        self.flag = flag

    def set_color(self, color):
        self.color = color

    def set_value(self, value):
        self.value = value

    def get_flag(self):
        return self.flag

    def get_color(self):
        return self.color

    def get_value(self):
        return self.value
