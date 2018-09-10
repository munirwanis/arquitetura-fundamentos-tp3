# #-*- coding:utf-8 -*-
'''
5) Usando a biblioteca Pygame, escreva um programa que desenha 1 quadrado verde de tamanho 50 na tela em posição aleatória (C).
'''

import sys, pygame
import random

pygame.init()

size = width, height = 800, 600
green = (0,255,0)

screen = pygame.display.set_mode(size)

x = random.randint(0,750)
y = random.randint(0,550)

pygame.draw.rect(screen, green, [x, y, 50, 50])

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pygame.display.update()