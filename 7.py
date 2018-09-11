# -*- coding:utf-8 -*-
'''
7) Usando a biblioteca Pygame, escreva um programa que desenha 1 quadrado de tamanho 50 e cor vermelha na tela. Quando for clicado, ele deve ser apagado da tela (C).
'''

import sys, pygame
import random

pygame.init()

size = width, height = 800, 600
red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

colors = [red, green, yellow, blue, white, pink]

screen = pygame.display.set_mode(size)

class Square():
    def __init__(self):
              self.width = 50
              self.height = 50
              self.x = random.randint(0, width-self.width)
              self.y = random.randint(0, height-self.height)
              self.area = pygame.Rect(self.x, self.y, self.width, self.height)
              self.color = red
    def draw(self, screen):
              pygame.draw.rect(screen, self.color, self.area)


square = Square()
square.draw(screen)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if square.area.collidepoint(pos):
                screen.fill(black)

    pygame.display.update()