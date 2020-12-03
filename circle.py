import random

import pygame

pygame.init()


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = [255, 0, 0]
        self.direction = "up"

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def resize(self):
        if self.direction == "down":
            self.radius -= 1
            if self.radius < 10:
                self.direction = "up"
        elif self.direction == "up":
            self.radius += 1
            if self.radius > 100:
                self.direction = "down"

    def recolor(self):
        rgb = random.randint(0, 2)
        if self.color[rgb] < 254:
            self.color[rgb] += 10
        if self.color[rgb] >= 254:
            self.color[rgb] = 0
