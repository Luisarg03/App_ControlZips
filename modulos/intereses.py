# -*- coding: utf-8 -*-
from os import remove
from os import path

pathsource = '/home/pentaho/AGIP/ARCHIVOS/Monsun/DatosSircreb/interesesUnion.txt'
pathtarget = '/home/pentaho/AGIP/ARCHIVOS/Monsun/DatosSircreb/InteresesFull.txt'
# pathsource = 'C:/Trabajo/Archivos/Sircreb_zips/interesesUnion.txt'
# pathtarget = 'C:/Trabajo/Archivos/Sircreb_zips/InteresesFull.txt'

if path.exists(pathtarget):
    remove(pathtarget)

with open(pathsource) as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    rows = list(content)

x = [0, 11, 4, 2, 1, 11, 22, 1, 18, 1, 18, 1, 5, 1, 18, 8, 38, 2]
y = [11, 15, 17, 18, 29, 51, 52, 70, 71, 89, 90, 95, 96, 114, 122, 160, 162]

full_list = []

for field in rows:
    n = 0
    lista = []
    for n1, n2 in zip(x, y):
        n = n + n1
        lista.append(field[n:n2])
    cadena = ';'.join(lista)

    full_list.append(cadena)

with open(pathtarget, 'a+') as f:
    for i in full_list:
        f.write(i+'\n')

if path.exists(pathsource):
    remove(pathsource)