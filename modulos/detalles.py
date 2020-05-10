# -*- coding: utf-8 -*-
from os import remove, path


def processDetalles(dir):
    '''Agrega la separacion de cada campo en los .txt de Detalles'''
    pathsource = dir + '/detalleUnion.txt'
    pathtarget = dir + '/DetallesFull.txt'

    if path.exists(pathtarget):
        remove(pathtarget)

    if path.exists(pathsource):
        with open(pathsource) as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            rows = list(content)

        # Lista de intervalos de caracacteres en los .txt que se tomara en cada iteracion.
        # Basado en la documentacion de la esctructura de los datos.
        x = [0, 11, 4, 2, 1, 11, 22, 1, 18, 1, 18, 1, 5, 1, 18, 8, 38, 2, 25]
        y = [11, 15, 17, 18, 29, 51, 52, 70, 71, 89, 90, 95, 96, 114, 122, 160, 162, 187]

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


def deleteDetalles():
    PATHS = ['/home/pentaho/AGIP/ARCHIVOS/Monsun/DatosSircreb',
             'C:/Trabajo/Archivos/Sircreb_zips']

    for pathtarget in PATHS:
        pathtarget = pathtarget + '/DetallesFull.txt'
        if path.exists(pathtarget):
            remove(pathtarget)
