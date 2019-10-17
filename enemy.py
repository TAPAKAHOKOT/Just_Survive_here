import pygame as pg
from random import randint
import math as m

class Enemy():
    """Создание класса враги"""
    def __init__(self, screen, settings, pers_x, pers_y):
        """Инициализация класса враги"""
        self.screen  = screen
        self.settings = settings

        self.rad = 4
        self.speed = 400

        self.pers_x = pers_x
        self.pers_y = pers_y

        self.color = (251,5,5)
        try:
            if randint(1, 2) == 1:
                self.x_cor = randint(0, self.pers_x - 100)
            else:
                self.x_cor = randint(self.pers_x + 100, settings.screen_width)
        except:
            self.x_cor = randint(0, settings.screen_width)

        try:
            if randint(1, 2) == 1:
                self.y_cor = randint(0, self.pers_y - 100)
            else:
                self.y_cor = randint(self.pers_y + 100, settings.screen_height)
        except:
            self.y_cor = randint(0, settings.screen_height)


        self.x = self.x_cor
        self.y = self.y_cor

    def draw(self):
        """Функция прорисовки врагов"""
        self.drawed_enemy = pg.draw.circle(self.screen, self.color, (self.x_cor, self.y_cor), self.rad)

    def update(self, pers_x, pers_y):
        """Функция обновления положения врагов"""
        self.pers_x = pers_x
        self.pers_y = pers_y

        self.gip = m.sqrt((self.pers_x - self.x)**2 + (self.pers_y - self.y)**2)

        self.speed_koef_x = self.x / self.gip
        self.speed_koef_y = self.y / self.gip
        # if abs(self.pers_x - self.x_cor) < 150 :
        #     self.speed -= 1
        #
        #     if self.speed <= 20:
        #         self.speed = 20

        self.x_step = (self.pers_x - self.x_cor)*2 / self.speed * self.speed_koef_x
        self.y_step = (self.pers_y - self.y_cor)*2 / self.speed * self.speed_koef_y

        self.x += self.x_step
        self.y += self.y_step

        self.x_cor = int(self.x)
        self.y_cor = int(self.y)
