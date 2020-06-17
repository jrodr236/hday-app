#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
hday és el joc del Hacking Day.
Aquest joc consisteix en superar una serie de proves.
Les proves estan organitzades en reptes.
Per superar cada prova s'ha d'indicar un codi correcte.

L'arquitectura de l'aplicació és en capes:
- Presentació: interacció amb l'usuari
- Lògica (de negoci): nucli de l'aplicació.
- Dades + Fitxers: interacció amb el SGBD i els fitxers
  - Dins de la capa de DADES s'utilitza el patró DAO
Per cadascuna de les capes hi ha un mòdul amb el nom adient.

Per simplificar, la verificació de les dades la realitzarà l'SBGD.
"""

from presentacio.general import mostrar_menu_principal, mostrar_capcalera, demanar_intro
from presentacio.errors import mostrar_error_control_c
from logica.administracio import administrar
from logica.joc import resoldre_reptes
from logica.general import demanar_usuari
from logica.monitoritzar import ranking, esdeveniments
from dades.usuari_dao import obtenir_punts


def main():
    """
    Programa principal
    """
    try:
        usuari = demanar_usuari()
        seguim = usuari is not None
        while seguim:
            obtenir_punts(usuari)
            mostrar_capcalera(usuari)
            opcio = mostrar_menu_principal(usuari.es_admin())
            if opcio == "a" and usuari.es_admin():
                administrar()
            elif opcio == "j":
                resoldre_reptes(usuari)
            elif opcio == "r":
                ranking()
            elif opcio == "e":
                esdeveniments()
            seguim = (opcio != "s")
    except KeyboardInterrupt:
        mostrar_error_control_c()
        demanar_intro()


if __name__ == "__main__":
    main()
