# #-*- coding:utf-8 -*-
'''
4) Usando a biblioteca Pygame, faça (C):

a) Crie uma janela com dimensões 800x600 (largura x altura).
b) Crie as cores vermelha, azul, branca, preta e amarela. Elas poderão ser usadas nos itens seguintes.
c) Faça seu programa esperar para fechar a janela até que o botão de sair seja clicado.
d) Desenhe um quadrado 100x100 de cor vermelha na tela na posição (100,10).
e) Desenhe um círculo de raio 50 de cor azul na tela na posição (400,300).
f) Escreva o texto “Quadrado” na cor amarela abaixo do desenho do quadrado.
g) Escreva o texto “Círculo” na cor branca dentro do círculo.
h) Insira o comando de atualização de tela com espera de 60Hz (use o clock.tick de um relógio previamente criado do módulo pygame). Depende do item 4c.
i) A cada 3 segundos (ou um valor aproximado), troque as cores do círculo e do quadrado. Depende do item 4c.
'''

import sys, pygame
pygame.init()

size = width, height = 800, 600
speed = [2, 2]
red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

screen = pygame.display.set_mode(size)
square = pygame.draw.rect(screen, red, [100, 10, 100, 100])
circle = pygame.draw.circle(screen, blue, [400, 300], 50)

default_font = pygame.font.get_default_font()
font = pygame.font.Font(default_font, 20)
square_text = font.render("Quadrado", True, yellow)
screen.blit(square_text, [100, 115])

circle_text = font.render("Círculo", True, white)
screen.blit(circle_text, [365, 293])
# ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # ballrect = ball.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

    # screen.fill(black)
    # screen.blit(ball, ballrect)
    pygame.display.flip()