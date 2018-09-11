# -*- coding:utf-8 -*-
'''
9) Usando a biblioteca Pygame, escreva um programa que desenha 10 quadrados de tamanho 50 na tela. Eles devem ter cores e posições aleatórias. 
Quando cada um deles for clicado, ele deve ser apagado da tela (C).
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
        self.color = colors[random.randint(0, len(colors)-1)]
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.area)


squares = []

for i in range(0, 10):
    square = Square()
    squares.append(square)
    square.draw(screen)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for square in squares:
                if square.area.collidepoint(pos):
                    squares.remove(square)
                    screen.fill(black, [square.x, square.y, square.width, square.height])

    pygame.display.update()