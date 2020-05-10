# -*- coding: utf-8 -*-
import zipfile
import glob
from os import remove, path


def descomprimir(clear, newzips, extract):
    '''Toma todos los zips del directorio y los descomprime de a uno por iteracion.
    Toda la informacion de cada uno de los .txt se agregan a cada archivo .txt
    correspondiente con su nombre.'''

    list_txt = glob.glob(clear)

    for i in list_txt:
        if path.exists(i):
            remove(i)

    with open(newzips) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        list_tmp = list(content)

    for i in list_tmp:
        ruta_zip = extract+i
        password = None
        archivo_zip = zipfile.ZipFile(ruta_zip, "r")
        archivos_txt = archivo_zip.namelist()
        archivo_zip.extractall(pwd=password, path=extract)

        for k in archivos_txt:

            pathsource = extract+k
            pathtarget = pathsource[:-4]+'Union'+pathsource[-4:]

            with open(pathsource) as f:
                content = f.readlines()
                content = [x.strip() for x in content]
                rows_tmp = list(content)
                rows = []

                for element in rows_tmp:
                    element = element+i[-24:]
                    rows.append(element)

            with open(pathtarget, 'a+') as f:
                for j in rows:
                    f.write(j+'\n')

            if path.exists(pathsource):
                remove(pathsource)
