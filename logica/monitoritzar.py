# -*- coding: utf-8 -*-

import time

from dades import ranking_dao, prova_superada_dao
from presentacio.monitoritzar import mostrar_ranking, mostrar_esdeveniments


def ranking():
    try:
        while True:
            rank = ranking_dao.obtenir()
            mostrar_ranking(rank)
            time.sleep(5)
    except KeyboardInterrupt:
        return


def esdeveniments():
    try:
        while True:
            proves_superades = prova_superada_dao.obtenir_proves()
            mostrar_esdeveniments(proves_superades)
            time.sleep(5)
    except KeyboardInterrupt:
        return
