from random import randint
import pygame as pg

class Grass():
    """Создание класса трав"""
    def __init__(self, screen, settings):
        """Инициализция класса трав"""
        self.color = (11,82,22)
        self.screen = screen
        self.x_cor = randint(0, settings.screen_width)
        self.y_cor = randint(0, settings.screen_height)
        self.grass_long = randint(1, 5)
        self.size = randint(1, 2)

    def draw(self):
        """Прорисовка трав"""
        self.drawed_grass = pg.draw.line(self.screen, self.color, (self.x_cor, self.y_cor), (self.x_cor, self.y_cor + self.grass_long) , self.size)
