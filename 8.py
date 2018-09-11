# -*- coding:utf-8 -*-
'''
8) Usando a biblioteca Pygame, escreva um programa que imprima (no terminal, usando print) a posição (x,y) dos cliques na tela (C).
'''

import sys, pygame
import random

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            print(pos)

    pygame.display.update()