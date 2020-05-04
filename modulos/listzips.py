import glob
from os import path, remove

PATH = 'C:/Trabajo/Archivos/Sircreb_zips'

########################################################
OLDZIPS = PATH + '/oldzips.csv'
NEWZIPS = PATH + '/newzips.csv'
CLEAR = PATH + '/*.txt'
ZIPS = PATH + '/*.zip'
EXTRACT = PATH+'/'


def createlistzips(dir, oldzip, newzip):
    if path.exists(oldzip):
        pass
    else:
        listzip = glob.glob(dir)
        namezip = []

        for row in listzip:
            row = row[-24:]
            namezip.append(row)

        with open(oldzip, 'a+') as f:
            for j in namezip:
                f.write(j+'\n')

        with open(newzip, 'a+') as f:
            for j in namezip:
                f.write(j+'\n')


def upgradelistzips(dir, oldzip, newzip):
    with open(oldzip) as f:
        content = f.readlines()
        content = [x.strip() for x in content]

        nameoldzip = []

        for i in content:
            nameoldzip.append(i)

    listzip = glob.glob(dir)
    namezip = []

    for row in listzip:
        row = row[-24:]
        namezip.append(row)

    compare = []

    for element in namezip:
        if element not in nameoldzip:
            compare.append(element)
        else:
            pass

    if path.exists(newzip):
        remove(newzip)

    with open(newzip, 'a+') as f:
        for j in compare:
            f.write(j+'\n')

    with open(oldzip, 'a+') as f:
        for k in compare:
            f.write(k+'\n')


createlistzips(ZIPS, OLDZIPS, NEWZIPS)
upgradelistzips(ZIPS, OLDZIPS, NEWZIPS)