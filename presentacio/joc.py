# -*- coding: utf-8 -*-

"""
Funcions de la capa de presentació relacioades amb el joc de Hacking Day.
"""

from presentacio.general import demanar_intro


def demanar_codi(repte):
    """
    Demana un codi per superar una prova d'un repte
    :param repte: repte del qual s'ha de superar la primera prova sense resoldre
    :return: codi indicat
    """
    codi = ""
    if repte.repte_superat():
        demanar_intro()
    else:
        codi = input("Codi (ENTER per sortir): ")

    print()
    return codi


def mostrar_codi_correcte(codi_correcte):
    """
    Indica que el codi introduït és correcte
    :param codi_correcte: True si el codi és correcte
    """
    if codi_correcte:
        print("OK. Codi correcte.")
    else:
        print("ERROR. Codi incorrecte.")
    demanar_intro()


def mostrar_prova_ja_superada():
    """
    Mostra que la prova ja s'havia superat en una altra instància enb execució d'aquesta aplicació.
    """
    print("Aquesta prova ja havia estat superada.")
    print("ATENCIÓ: no facis trampes!")
    demanar_intro()


def mostrar_proves_per_superar(repte):
    """
    Mostra les proves superades i la primera prova per superar d'un repte
    :param repte: repte del qual s'han de mostrar les proves
    """
    titol = "Repte: {}".format(repte.nom)
    print(titol)
    print("-" * len(titol))
    print()

    ordre_per_mostrar = 1
    for p in repte.proves:
        print("* Prova {} (#{}) *".format(ordre_per_mostrar, p.ordre))
        ordre_per_mostrar += 1
        print(p.enunciat)
        if p.superada:
            print("[PROVA SUPERADA]")
            print()
        else:
            # Prova no superada, no s'han d'ensenyar més
            break
