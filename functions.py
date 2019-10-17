import pygame as pg
import sys
from grass import Grass
from defend import Def_dots, Def_dots_box, Def_dots_x_size_box
import time as t
from random import randint
from enemy import Enemy
import tkinter as tk

moving = [False, False, False, False]


def screen_update(screen, settings, pers):
    """Функция обновления игровой информации и положения тел"""
    screen.fill((settings.screen_color))

    settings.fps = round(settings.clock.get_fps())
    settings.kadr += 1
    settings.all_fps += settings.fps

    if settings.time % 2 == 0:
        settings.kadr //=2
        settings.all_fps //= 2

    if randint(1,5000) == 300:
        create_def_dots_x_size_box(screen, settings)

    if settings.score > 50:
        settings.enemies_num_creating = 2

    if settings.score > 100:
        settings.enemies_num_creating = 4

    fonts_update(screen, settings)

    """Создание врага каждую секунду"""
    if round(t.clock()) - 1 * settings.time == 0:
        settings.score += 1
        settings.time += 1
        create_enemy(screen, settings, pers)

    for grass in settings.grasses:
        grass.draw()

    for box in settings.def_dots_boxes:
        box.draw()

    for enemy in settings.enemies_list:
        enemy.draw()
        enemy.update(pers.x_cor, pers.y_cor)

    pers.update()
    pers.draw()

    """Проверка элементов на столкновения"""
    for i in settings.enemies_list:
        for k in settings.enemies_list:
            if i != k:
                if i.drawed_enemy.clip(k.drawed_enemy):
                    settings.enemies_list.remove(i)
                    settings.enemies_list.remove(k)
                    settings.score += 4

        if i.drawed_enemy.clip(pers.drawed_pers):
            death_event(screen, settings)
            settings.enemies_num_creating = 1
            settings.enemies_list.clear()
            settings.def_dots.clear()
            settings.scores.append(settings.score)
            settings.score = 0
            # create_lose_win(screen, settings)

        for k in settings.def_dots:
            if k.drawed_def_dot.clip(i.drawed_enemy):
                try:
                    settings.enemies_list.remove(i)
                except:
                    print("Error str 72")
                settings.score += 2


    for i in settings.def_dots_x_size_boxes:
        if i.drawed_box.clip(pers.drawed_pers):
            settings.def_dots_x_size_boxes.remove(i)
            for k in settings.def_dots:
                k.rad = 15
                k.v = 1
        i.draw()

    for i in settings.def_dots_boxes:

        if i.drawed_box.clip(pers.drawed_pers):
                settings.def_dots_boxes.remove(i)
                create_box(screen, settings)
                if len(settings.def_dots) < 3:
                    create_new_def_dots(screen, settings, pers)

    """Удаление защитных точек по истечению 15 секунд после их появления"""

    for def_dot in settings.def_dots:
        if t.clock() - def_dot.time >= 15:
            def_dot.rad -= 1
            if def_dot.rad <= 1:
                settings.def_dots.remove(def_dot)
                continue
        def_dot.draw()

        def_dot.update()

    pg.display.flip()


def create_lose_win(screen, settings):
    """Функция заверения игры"""
    print(0)

def create_enemy(screen, settings, pers):
    """Создание вражеских объектов"""
    for k in range(settings.enemies_num_creating):
        enemy = Enemy(screen, settings, pers.x_cor, pers.y_cor)

        settings.enemies_list.append(enemy)

        enemy.draw()

def create_grass(screen, settings):
    """Создание травы"""
    for i in range(settings.grasses_number):
        grass = Grass(screen, settings)

        settings.grasses.append(grass)

def create_box(screen, settings):
    """Создание коробок с защитой"""
    box = Def_dots_box(screen, settings)

    settings.def_dots_boxes.append(box)

    box.draw()


def create_new_def_dots(screen, settings, pers):
    """Создание защитных точек"""
    pos = randint(0, 2)

    def_dot = Def_dots(screen, settings, pos, pers)

    settings.def_dots.append(def_dot)

def create_def_dots_x_size_box(screen, settings):
    """Создание защитных точек"""
    box = Def_dots_x_size_box(screen, settings)

    settings.def_dots_x_size_boxes.append(box)

    box.draw()

def fonts_update(screen, settings):
    font = pg.font.SysFont(settings.font, 50)
    textSurfaceObj = font.render(str(settings.score),
                                                True, (0,0,0), (29,125,44))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (settings.screen_width//2, 100)

    font2 = pg.font.SysFont(settings.font, 10)
    textSurfaceObj2 = font2.render("fps: " + str(round(settings.fps)),
                                                    True, (0,0,0), (29,125,44))
    textRectObj2 = textSurfaceObj.get_rect()
    textRectObj2.center = (50, 30)

    screen.blit(textSurfaceObj, textRectObj)
    screen.blit(textSurfaceObj2, textRectObj2)

"""--------------------------"""
def death_event(screen, settings):
    t.sleep(1)


def check_events(screen, settings, pers):
    """Проверка событий клавиатуры и мыши"""
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            check_events_down(screen, settings, pers, event)
        if event.type == pg.KEYUP:
            check_events_up(screen, settings, pers, event)


        if event.type == pg.QUIT:
            sys.exit()

def check_events_down(screen, settings, pers, event):
    """Проверка событий нажатия кнопки"""
    if event.key == pg.K_ESCAPE:
        settings.scores.append(settings.score)

        print('\n\n', '-' * 44)
        print("Your max score is: {}".format( max(settings.scores) ))
        print('-' * 44, '\n\n')
        print('The average fps: {}'.format( round(settings.all_fps / settings.kadr) ))

        sys.exit()

    if event.key == pg.K_d:
          pers.moving_right = True
    elif event.key == pg.K_a:
          pers.moving_left = True
    elif event.key == pg.K_w:
          pers.moving_up = True
    elif event.key == pg.K_s:
          pers.moving_down = True

def check_events_up(screen, settings, pers, event):
    """Проверка событий отпускания кнопки"""
    if event.key == pg.K_d:
          pers.moving_right = False
    elif event.key == pg.K_a:
          pers.moving_left = False
    elif event.key == pg.K_w:
          pers.moving_up = False
    elif event.key == pg.K_s:
          pers.moving_down = False
