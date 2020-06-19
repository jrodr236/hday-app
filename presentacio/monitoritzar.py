# -*- coding: utf-8 -*-

from datetime import datetime
from typing import List

from logica.entitats import ProvaSuperada
from .general import neteja_pantalla


def mostra_ranking(ranking):
    neteja_pantalla()
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
        print(" - " + tipus, end="")
        print(" ({})".format(data.strftime('%d/%m/%Y %H:%M:%S')))
        i = i + 1
    print()
    print("En cas d'empat de punts, guanya qui hagi superat abans la seva última prova.")
    print("^C per sortir")


def mostra_esdeveniments(proves_superades: List[ProvaSuperada]):
    neteja_pantalla()
    print("Últims esdeveniments ({})".format(datetime.now().strftime('%H:%M:%S')))
    print("--------------------")
    for ps in proves_superades:
        print(ps.data.strftime("%d/%m/%Y %H:%M:%S"), end="")
        print(": {} ({}) ha superat {} #{} - {} punts.".format(ps.usuari.nom, ps.usuari.tipus, ps.prova.repte.nom,
                                                               ps.prova.ordre, ps.prova.puntuacio))
    print()
    print("^C per sortir")
