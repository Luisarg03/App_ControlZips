# -*- coding: utf-8 -*-
from os import remove
from os import path


def processPagos(dir):
    '''Agrega la separacion de cada campo en los .txt de Pagos'''
    pathsource = dir + '/pagosUnion.txt'
    pathtarget = dir + '/PagosFull.txt'

    if path.exists(pathtarget):
        remove(pathtarget)

    with open(pathsource) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        rows = list(content)

    # Lista de intervalos de caracacteres en los .txt que se tomara en cada iteracion.
    # Basado en la documentacion de la esctructura de los datos.
    x = [0, 11, 4, 2, 1, 8, 38, 2, 18, 1, 18, 1, 18, 25]
    y = [11, 15, 17, 18, 26, 64, 66, 84, 85, 103, 104, 122, 147]

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
