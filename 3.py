# #-*- coding:utf-8 -*-
'''
3) Escreva um programa em Python que leia um vetor de 10 palavras e 
mostre-as na ordem inversa de leitura (C).
'''

array = [
    "Uma palavra",
    "Duas palavras",
    "Três palavras",
    "Quatro palavras",
    "Cinco palavras",
    "Seis palavras",
    "Sete palavras",
    "Oito palavras",
    "Nove palavras",
    "Dez palavras"
    ]

for i in range(0, len(array)):
    print(array[i][::-1])