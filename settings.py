import pygame as pg
import time as t


class Settings():
    def __init__(self, clock):
        """Настройки размера поля"""
        self.screen_height = 108
        self.screen_width = 192

        #Настройка цвета поля
        self.screen_color = (29,125,44)

        #Настройка цвета травы
        self.grasses_number = 100

        #Настройка стартовых очков
        self.score = 0
        self.scores = []

        self.time = 1

        #Создание игровых списков
        self.grasses = []
        self.def_dots = []

        self.p = 100
        self.def_dots_a = [100, 150, 200]
        self.def_dots_b = [50, 100, 150]
        self.def_dots_speed = [0.3, 0.15, 0.2]

        self.def_dot_num = 0

        self.def_dots_boxes = []

        self.def_dots_x_size_boxes = []

        self.enemies_list = []

        self.kadr = 0

        self.enemies_num_creating = 1

        self.font = 'arial'

        self.fps = 0
        self.clock = clock

        self.all_fps = 0
