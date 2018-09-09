# #-*- coding:utf-8 -*-
'''
# 1) Usando Python, faça o que se pede (C e PS):

a) Crie uma lista vazia;
b) Adicione os elementos: 1, 2, 3, 4 e 5, usando o append;
c) Imprima a lista;
d) Agora, remova os elementos ‘3’ e ‘6’ (não esqueça de checar se eles estão na lista);
e) Imprima a lista modificada;
f) Imprima também o tamanho da lista usando a função len;
g) Altere o valor do último elemento para 6 e imprima a lista modificada.
'''

array = []

array.append(1)
array.append(2)
array.append(3)
array.append(4)
array.append(5)

print(array)

if 3 in array: array.remove(3)
if 6 in array: array.remove(6)

print(array)
print(f'Tamanho: {len(array)}')

array[:] = [6 if x == array[-1] else x for x in array]
print(array)