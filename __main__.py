#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dades.usuari_dao import obtenir_punts
from logica.joc import resoldre_reptes
from logica.monitoritzar import ranking, esdeveniments
from logica.usuari import demanar_usuari
from presentacio.errors import mostrar_error_control_c
from presentacio.general import mostrar_menu_principal, mostrar_capcalera, demanar_intro


def main():
    try:
        usuari = demanar_usuari()
        seguim = usuari is not None
        while seguim:
            obtenir_punts(usuari)
            mostrar_capcalera(usuari)
            opcio = mostrar_menu_principal()
            if opcio == "j":
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
