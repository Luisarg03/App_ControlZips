# -*- coding: utf-8 -*-
from modulos.listzips import createlistzips, upgradelistzips
from modulos.zips import descomprimir
from modulos.cabeceras import processCabeceras
from modulos.detalles import processDetalles
from modulos.pagos import processPagos
from modulos.intereses import processIntereses

# Var. Produccion
# PATH = '/home/pentaho/AGIP/ARCHIVOS/Monsun/DatosSircreb'

# Var. Desarrollo
PATH = 'C:/Trabajo/Archivos/Sircreb_zips'

########################################################
OLDZIPS = PATH + '/zips_cargados.csv'
NEWZIPS = PATH + '/zips_nuevos.csv'
CLEAR = PATH + '/*.txt'
ZIPS = PATH + '/*.zip'
EXTRACT = PATH+'/'


def main():
    createlistzips(ZIPS, OLDZIPS, NEWZIPS)
    upgradelistzips(ZIPS, OLDZIPS, NEWZIPS)
    descomprimir(CLEAR, NEWZIPS, EXTRACT)
    processCabeceras(PATH)
    processDetalles(PATH)
    processPagos(PATH)
    processIntereses(PATH)


if __name__ == '__main__':
    main()
