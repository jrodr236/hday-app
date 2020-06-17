# -*- coding: utf-8 -*-

"""
Funcions de la capa de lògica de negoci relacionades amb el joc de Hacking Day.
"""

from logica.entitats import ProvaJaSuperada
from presentacio.general import *
from presentacio.joc import *
from dades import prova_dao, repte_dao, usuari_dao


def resoldre_reptes(usuari):
    """
    Funció que permet jugar al joc, que consisteix en resoldre reptes, prova a prova.
    :param usuari: usuari que utilitza l'aplicació
    """
    while True:
        usuari_dao.obtenir_punts(usuari)
        mostrar_capcalera(usuari)
        reptes = repte_dao.obtenir_reptes(usuari)
        mostrar_reptes(reptes, False, True)
        repte = escollir_repte(reptes)

        if repte is None:
            continue
        elif repte == "s":
            return

        respondre_prova(usuari, repte)


def respondre_prova(usuari, repte):
    """
    Permet a l'usuari resoldre la següent prova no resolta del repte actual
    :param usuari: usuari que utilitza l'aplicació
    :param repte: repte que es vol resoldre
    """
    while True:
        usuari_dao.obtenir_punts(usuari)
        mostrar_capcalera(usuari)
        # S'actualitzen les proves per si hi ha hagut alguna actualització, per exemple, si s'ha resolt alguna prova
        # en un altre execució del joc.
        prova_dao.obtenir_proves_de_repte(repte, usuari)
        prova_per_resoldre = repte.dona_prova_sense_resoldre()
        mostrar_proves_per_superar(repte)
        codi = demanar_codi(repte)

        if codi == "":
            break

        try:
            # Per disseny de la BBDD, no es permet que es resolgui una prova dues vegades. Si això hagués de passar,
            # es llançarà l'excepció ProvaJaSuperada i no es realitza la transacció.
            codi_correcte = prova_dao.verificar_codi(prova_per_resoldre, usuari, codi)

            if codi_correcte:
                prova_per_resoldre.superar()

            mostrar_codi_correcte(codi_correcte)
        except ProvaJaSuperada:
            mostrar_prova_ja_superada()
            return
