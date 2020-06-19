# -*- coding: utf-8 -*-

"""
Funcions de la capa de presentació relacionades amb la monitorització del joc, és a dir, el rànking i els últims
esdeveniments.
"""

from typing import List

from datetime import datetime

from logica.entitats import ProvaSuperada
from .general import netejar_pantalla


def mostrar_ranking(ranking):
    netejar_pantalla()
    print("Ranking ({})".format(datetime.now().strftime('%H:%M:%S')))
    print("-------")
    i = 1
    for lin in ranking:
        nom = lin[0]
        tipus = lin[1]
        punts = lin[2]
        data = lin[3]
        print("{}. {}".format(i, nom), end="")
        print("." * (20 - (len(nom) + len(str(punts)))), end="")
        print(punts, end="")
        print(" - "+tipus, end="")
        print(" ({})".format(data.strftime('%d/%m/%Y %H:%M:%S')))
        i = i + 1
    print()
    print("En cas d'empat de punts, guanya qui hagi superat abans la seva última prova.")
    print("^C per sortir")


def mostrar_esdeveniments(proves_superades: List[ProvaSuperada]):
    netejar_pantalla()
    print("Últims esdeveniments ({})".format(datetime.now().strftime('%H:%M:%S')))
    print("--------------------")
    for ps in proves_superades:
        print(ps.data.strftime("%d/%m/%Y %H:%M:%S"), end="")
        print(": {} ({}) ha superat {} #{} - {} punts.".format(ps.usuari.nom, ps.usuari.tipus, ps.prova.repte.nom, ps.prova.ordre, ps.prova.puntuacio))
    print()
    print("^C per sortir")
