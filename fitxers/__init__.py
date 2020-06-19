# -*- coding: utf-8 -*-


import csv
import os

from logica.entitats import Repte, Prova


def es_ruta_correcta(ruta):
    return os.path.exists(ruta)


def llegir_fitxer_csv(ruta):
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
            prova = Prova(repte, int(r[1]), r[2], r[3], r[4], int(r[5]), False)
            repte.afegeix_prova(prova)

    f.close()

    return reptes
