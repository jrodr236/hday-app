# -*- coding: utf-8 -*-


from app.dades import repte_dao
from app.fitxers import *
from app.presentacio.administracio import *
from app.presentacio.errors import *
from app.presentacio.general import *


def importar_proves_csv(ruta=None):
    if ruta is None:
        ruta = demana_ruta_csv_per_importar_dades()

    if not es_ruta_correcta(ruta):
        mostra_error_ruta_fitxer()
        return

    try:
        reptes = llegir_fitxer_csv(ruta)
        repte_dao.desar_reptes_i_les_seves_proves(reptes)
        mostra_accio_realitzada()
    except Exception as e:
        mostrar_error_lectura_fitxer(e)
        demana_intro()
