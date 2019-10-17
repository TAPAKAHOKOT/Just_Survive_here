import pygame as pg
from random import randint
import math
import time as t

class Def_dots():
    """Создание класса защиты"""
    def __init__(self, screen, settings, i, pers):
        """Инициализация класса защиты"""
        self.def_dot_settings = settings
        self.screen = screen

        self.rad = 5
        self.i = i

        self.a = self.def_dot_settings.def_dots_a[self.i]
        self.b = self.def_dot_settings.def_dots_b[self.i]

        self.v = self.def_dot_settings.def_dots_speed[self.i]
        self.t = 1
        self.koef = -1
        self.a_t = self.a
        self.b_t = self.b

        # self.f = self.rocket_settings.ugol[i]
        self.f = 1

        self.time = t.clock()

        self.color = (0,0,0)

        self.x_cor = 500
        self.y_cor = 580

        self.x_0 = pers.x_cor
        self.y_0 = pers.y_cor

        self.x = self.x_cor
        self.y = self.y_cor

    def draw(self):
        """Прорисовка защитных точек"""
        self.drawed_def_dot = pg.draw.circle(self.screen, self.color, (self.x, self.y), self.rad)

    def update(self):
        """Обновление защитных точек"""
        self.x_cor = self.a*math.cos(self.v*self.t + self.f) + self.x_0
        self.y_cor = self.b*math.sin(self.v*self.t) + self.y_0


        self.t += 0.1


        self.x = int(self.x_cor)
        self.y = int(self.y_cor)

class Def_dots_box():
    """Создание класса зщитных коробок"""
    def __init__(self, screen, settings):
        """Инициализация класса защитных коробок"""
        self.screen = screen
        self.settings = settings
        self.size = 12
        self.color = (245,255,0)
        self.inside_color = (0,0,0)
        self.x_cor = randint(0, self.settings.screen_width - self.size)
        self.y_cor = randint(0, self.settings.screen_height - self.size)


    def draw(self):
        """Прорисовка защитных коробок"""
        self.drawed_box = pg.draw.rect(self.screen, (self.color), ((self.x_cor, self.y_cor), (self.size, self.size)))

        self.drawed_def_inside = pg.draw.rect(self.screen, (self.inside_color), ((self.x_cor + self.size // 3, self.y_cor + self.size // 3),
        (self.size//3, self.size//3)))

class Def_dots_x_size_box():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.size = 12
        self.color = (254,110,0)
        self.inside_color = (0,0,0)
        self.x_cor = randint(0, self.settings.screen_width - self.size)
        self.y_cor = randint(0, self.settings.screen_height - self.size)

    def draw(self):
        """Прорисовка защитных коробок"""
        self.drawed_box = pg.draw.rect(self.screen, (self.color), ((self.x_cor, self.y_cor), (self.size, self.size)))

        self.drawed_def_inside = pg.draw.rect(self.screen, (self.inside_color), ((self.x_cor + self.size // 3, self.y_cor + self.size // 3),
        (self.size//3, self.size//3)))
