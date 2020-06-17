# -*- coding: utf-8 -*-

"""
Funcions que interaccionen amb el sistema de fitxers
"""

import csv
import os

from logica.entitats import Repte, Prova


def ruta_correcta(ruta):
    """
    Verifica si existeix aquesta ruta
    :param ruta: ruta a verificar
    """
    return os.path.exists(ruta)


def llegir_fitxer(ruta):
    """
    Llegeix el fitxer CSV i li extreu els reptes i proves
    :param ruta: fitxer CSV a llegir
    :return: conjunt de reptes, amb proves associades, que s'han extret del fitxer
    """
    f = open(ruta, 'r+')

    reptes = []
    with open(ruta, newline='') as fitxer:
        lector = csv.reader(fitxer, delimiter=',', quotechar='"')
        for r in lector:
            nom_repte = r[0]
            repte = next((x for x in reptes if x.nom == nom_repte), None)
            if repte is None:
                repte = Repte(nom_repte)
                reptes.append(repte)
            prova = Prova(repte, r[1], r[2], r[3], r[4], r[5], False)
            repte.afegeix_prova(prova)

    f.close()

    return reptes
