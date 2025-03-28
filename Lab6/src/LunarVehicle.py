import math


class LunarVehicle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0

    def start_position(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def get_position(self):
        return self.x, self.y, self.angle

    def go_forward(self, distance=1):
        radian_angle = math.radians(self.angle)

        self.x += math.cos(radian_angle) * distance
        self.y += math.sin(radian_angle) * distance

    def go_back(self, distance=1):
        radian_angle = math.radians(self.angle)

        self.x -= math.cos(radian_angle) * distance
        self.y -= math.sin(radian_angle) * distance

    def rotation(self, angle):
        self.angle = (self.angle + angle) % 360