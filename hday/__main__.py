#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hday.presentacio.general import mostrar_menu_principal, mostrar_capcalera, demanar_intro
from hday.presentacio.errors import mostrar_error_control_c
from hday.logica.administracio import administrar
from hday.logica.joc import resoldre_reptes
from hday.logica.general import demanar_usuari
from hday.logica.monitoritzar import ranking, esdeveniments
from hday.dades.usuari_dao import obtenir_punts


def main():
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
