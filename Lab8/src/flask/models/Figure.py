from abc import ABC

class Figure(ABC):
    def __init__(self, name: str):
        self.name = name
        self.color = "#808080"

    def get_name(self) -> str:
        return self.name

    def get_color(self) -> str:
        return self.color

    def update_color(self, color: str):
        self.color = color