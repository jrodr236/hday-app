# -*- coding: utf-8 -*-
import time

import dades.prova_superada_dao

"""
Funcions de la capa de lògica de negoci relacionades amb la monitoritació de l'aplicació, és a dir, el rànking
i els esdeveniments.
"""

from dades import ranking_dao
from presentacio.monitoritzar import mostrar_ranking, mostrar_esdeveniments


def ranking():
    """
    Mostra els millors participants i els punts que porten acumulats.
    """
    try:
        while True:
            rank = ranking_dao.obtenir()
            mostrar_ranking(rank)
            time.sleep(5)
    except KeyboardInterrupt:
        return


def esdeveniments():
    """
    Mostra les últimes proves resoltes
    """
    try:
        while True:
            proves_superades = dades.prova_superada_dao.obtenir()
            mostrar_esdeveniments(proves_superades)
            time.sleep(5)
    except KeyboardInterrupt:
        return
