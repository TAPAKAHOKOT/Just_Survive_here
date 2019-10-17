import pygame as pg
from defend import Def_dots


class Pers():
    """Создание класса персонаж"""
    def __init__(self, screen, settings):
        """Инициализация класса персонаж"""
        self.size_x = 8
        self.size_y = 8
        self.pers_speed = 4
        self.screen = screen
        self.pers_settings = settings

        self.x_cor = self.pers_settings.screen_width//2 - self.size_x//2
        self.y_cor = self.pers_settings.screen_height//2 - self.size_y//2

        # self.color = (104,60,144)
        self.color = (23,27,162)

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False


    def draw(self):
        """Прорисовка персонажа"""
        self.drawed_pers = pg.draw.rect(self.screen, self.color,((self.x_cor, self.y_cor), (self.size_x, self.size_y)))

    def update(self):
        """Обновление положения персонажа"""
        for i in self.pers_settings.def_dots:
            i.x_0 = self.x_cor
            i.y_0 = self.y_cor

        if self.moving_left and self.x_cor > 0:
            self.x_cor -= self.pers_speed



        if self.moving_right and self.x_cor < self.pers_settings.screen_width - self.size_x:
            self.x_cor += self.pers_speed

        if self.moving_up and self.y_cor > 0:
            self.y_cor -= self.pers_speed

        if self.moving_down and self.y_cor < self.pers_settings.screen_height - self.size_y:
            self.y_cor += self.pers_speed
