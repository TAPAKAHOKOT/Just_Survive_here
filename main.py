import pygame as pg
from settings import Settings
import functions as fu
from pers import Pers
from defend import Def_dots
import time as t
import tkinter as tk
import os

t.perf_counter()

def run_game():
    """Функция запуска приложения"""
    # Инициализация pygame экрана
    pg.init()

    os.system('cls')
    #Видимость мыши устанавливается на невидимую
    pg.mouse.set_visible(False)
    # Присвоение переменной значения класса настроек
    settings = Settings(pg.time.Clock())

    # clock = pg.time.Clock()

    # Определение размеров экрана и передача этих значений в настройки
    root = tk.Tk()

    settings.screen_width = root.winfo_screenwidth()
    settings.screen_height = root.winfo_screenheight()

    # Создания экрана pygame
    screen = pg.display.set_mode((
                                    settings.screen_width, settings.screen_height
                                ), pg.FULLSCREEN)
    # Создание объектов приложения
    fu.create_grass(screen, settings)
    pers = Pers(screen, settings)
    fu.create_box(screen, settings)
    fu.create_enemy(screen, settings, pers)

    # clock =


    # Запуск цикла игрыwww
    while True:
        settings.clock.tick(150)
        # обновление экрана
        fu.screen_update(screen, settings, pers)
        # функция проверки событий
        fu.check_events(screen, settings, pers)

# Запуск игры
run_game()
