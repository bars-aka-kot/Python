import math
from typing import Any


class Dragon:
    def __init__(self, height, fire_danger, color):
        self.height = height
        self.danger = fire_danger
        self.color = color

    def __gt__(self, other):
        if type(other) == Dragon:
            if (self.height > other.height) or (self.danger > other.danger) or (self.color > other.color):
                return True
            else:
                return False

    def __ne__(self, other):
        if type(other) == Dragon:
            if (self.height != other.height) or (self.danger != other.danger) or (self.color != other.color):
                return True
            else:
                return False

    def __le__(self, other):
        if type(other) == Dragon:
            if (self.height <= other.height) or (self.danger <= other.danger) or (self.color <= other.color):
                return True
            else:
                return False

    def __add__(self, other):
        if type(other) == Dragon:
            new_height = math.floor((self.height + other.height)/2)
            new_danger = max(self.danger, other.danger)
            new_color = min(self.color, other.color)
            return Dragon(new_height, new_danger, new_color)

    def __str__(self):
        return f"Dragon with height {self.height}, danger {self.danger} and color {self.color}."

    def change_color(self, color):
        self.color = color

    def __isub__(self, number):
        self.height -= self.height // number
        self.danger += self.danger % number
        return self

    def __repr__(self):
        return f"{self.height} {self.danger} {self.color}"

    def __call__(self, string):
        return string * self.danger


dr1 = Dragon(69, 5, "brown")
dr2 = Dragon(69, 5, "gray")
print(dr1 > dr2, dr1 != dr2, dr1 <= dr2)
print(dr1, dr2, sep="\n")
print()
dr1.change_color("white")
dr1 -= 23
dr2 -= 2
dr3 = dr1 + dr2
print(dr1, dr2, dr3, sep="\n")
print(dr1("Welcome"))
