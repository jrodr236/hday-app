#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
