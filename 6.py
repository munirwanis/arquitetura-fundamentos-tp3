# #-*- coding:utf-8 -*-
'''
6) Usando a biblioteca Pygame, escreva um programa que desenha 10 quadrados de tamanho 50 na tela. Eles devem ter cores e posições aleatórias (C).
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

for i in range(0, 10):
    x = random.randint(0,750)
    y = random.randint(0,550)
    random_color = colors[random.randint(0, len(colors)-1)]

    pygame.draw.rect(screen, random_color, [x, y, 50, 50])

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pygame.display.update()