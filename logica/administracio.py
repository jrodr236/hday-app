# -*- coding: utf-8 -*-


from dades import repte_dao
from fitxers import *
from presentacio.administracio import *
from presentacio.errors import *
from presentacio.general import *


def importar_proves_csv(ruta=None):
    if ruta is None:
        ruta = demanar_ruta_csv_per_importar_dades()

    if not es_ruta_correcta(ruta):
        mostrar_error_ruta_fitxer()
        return

    try:
        reptes = llegir_fitxer_csv(ruta)
        repte_dao.desar_reptes_i_les_seves_proves(reptes)
        mostrar_accio_realitzada()
    except Exception as e:
        mostrar_error_lectura_fitxer(e)
        demanar_intro()
