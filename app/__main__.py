#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app.dades.usuari_dao import obtenir_punts
from app.logica.joc import jugar
from app.logica.monitoritzar import ranking, esdeveniments
from app.logica.usuari import demanar_usuari
from app.presentacio.errors import mostrar_error_control_c
from app.presentacio.general import mostra_menu_principal, mostra_capcalera, demana_intro


def main():
    try:
        usuari = demanar_usuari()
        seguim_jugant = usuari is not None
        while seguim_jugant:
            obtenir_punts(usuari)
            mostra_capcalera(usuari)
            opcio = mostra_menu_principal()
            if opcio == "j":
                jugar(usuari)
            elif opcio == "r":
                ranking()
            elif opcio == "e":
                esdeveniments()
            seguim_jugant = (opcio != "s")
    except KeyboardInterrupt:
        mostrar_error_control_c()
        demana_intro()


if __name__ == "__main__":
    main()
