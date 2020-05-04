# -*- coding: utf-8 -*-
from os import remove
from os import path


def processIntereses(dir):
    '''Agrega la separacion de cada campo en los .txt de Intereses'''
    pathsource = dir + '/interesesUnion.txt'
    pathtarget = dir + '/InteresesFull.txt'

    if path.exists(pathtarget):
        remove(pathtarget)

    if path.exists(pathsource):
        with open(pathsource) as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            rows = list(content)

        x = [0, 11, 4, 2, 1, 8, 38, 1, 18, 25]
        y = [11, 15, 17, 18, 26, 64, 65, 83, 108]   

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

    else:
        pass
