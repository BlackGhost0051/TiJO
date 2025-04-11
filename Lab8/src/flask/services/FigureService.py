from Lab8.src.flask.models.Figure import  Figure
from Lab8.src.flask.models.Square import Square
from Lab8.src.flask.models.Circle import Circle
from Lab8.src.flask.models.Triangle import Triangle

class FigureService:
    def __init__(self):
        self.figures = {
            "square": Square(),
            "circle": Circle(),
            "triangle": Triangle()
        }

    def get_figure(self, name: str) -> Figure:
        return self.figures.get(name)

    def update_figure_color(self, name: str, color: str) -> bool:
        figure = self.get_figure(name)
        if figure:
            figure.update_color(color)
            return True
        return False

    def update_all_colors(self, color: str):
        for figure in self.figures.values():
            figure.update_color(color)

    def get_colors(self) -> dict:
        return {name: fig.get_color() for name, fig in self.figures.items()}
