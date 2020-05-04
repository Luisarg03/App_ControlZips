# -*- coding: utf-8 -*-
from modulos.listzips import createlistzips, upgradelistzips
from modulos.zips import descomprimir
from modulos.cabeceras import processCabeceras
from modulos.detalles import processDetalles
from modulos.pagos import processPagos

# Var. Produccion
# PATH = '/home/pentaho/AGIP/ARCHIVOS/Monsun/DatosSircreb'

# Var. Desarrollo
PATH = 'C:/Trabajo/Archivos/Sircreb_zips'

########################################################
OLDZIPS = PATH + '/oldzips.csv'
NEWZIPS = PATH + '/newzips.csv'
CLEAR = PATH + '/*.txt'
ZIPS = PATH + '/*.zip'
EXTRACT = PATH+'/'


def main():
    createlistzips(ZIPS, OLDZIPS, NEWZIPS)
    upgradelistzips(ZIPS, OLDZIPS, NEWZIPS)
    descomprimir(CLEAR, ZIPS, EXTRACT)
    processCabeceras(PATH)
    processDetalles(PATH)
    processPagos(PATH)


if __name__ == '__main__':
    main()
