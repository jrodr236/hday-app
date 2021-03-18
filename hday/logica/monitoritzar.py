# -*- coding: utf-8 -*-

import time

from dades import ranking_dao, prova_superada_dao
from presentacio.monitoritzar import mostra_ranking, mostra_esdeveniments


def ranking():
    try:
        while True:
            rank = ranking_dao.obtenir()
            mostra_ranking(rank)
            time.sleep(5)
    except KeyboardInterrupt:
        return


def esdeveniments():
    try:
        while True:
            proves_superades = prova_superada_dao.obtenir_proves()
            mostra_esdeveniments(proves_superades)
            time.sleep(5)
    except KeyboardInterrupt:
        return
