# -*- coding: utf-8 -*-
from modulos.listzips import createlistzips, upgradelistzips
from modulos.zips import descomprimir
from modulos.cabeceras import processCabeceras, deleteCabeceras
from modulos.detalles import processDetalles, deleteDetalles
from modulos.pagos import processPagos, deletePagos
from modulos.intereses import deleteIntereses, processIntereses

# Var. Produccion
PATH = '/home/pentaho/AGIP/ARCHIVOS/Monsun/DatosSircreb'

# Var. Desarrollo
# PATH = 'C:/Trabajo/Archivos/Sircreb_zips'

########################################################
try:
    OLDZIPS = PATH + '/zips_cargados.csv'
    NEWZIPS = PATH + '/zips_nuevos.csv'
    CLEAR = PATH + '/*.txt'
    ZIPS = PATH + '/*.zip'
    EXTRACT = PATH + '/'
except NameError:
    pass


def main():
    try:
        createlistzips(ZIPS, OLDZIPS, NEWZIPS)
        upgradelistzips(ZIPS, OLDZIPS, NEWZIPS)
        descomprimir(CLEAR, NEWZIPS, EXTRACT)
        processCabeceras(PATH)
        processDetalles(PATH)
        processPagos(PATH)
        processIntereses(PATH)
    except (NameError, IOError):
        deleteCabeceras()
        deleteDetalles()
        deletePagos()
        deleteIntereses()


if __name__ == '__main__':
    main()
