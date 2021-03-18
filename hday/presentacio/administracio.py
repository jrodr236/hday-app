# -*- coding: utf-8 -*-

from .general import demana_intro


def demana_ruta_csv_per_importar_dades():
    print("El format de les files del fitxer per carregar les proves ha de ser:")
    print("nom prova,ordre,tipus_usuari(NULL/gm/gs),enunciat,codi,puntuacio")
    print()
    ruta = input("Introdueix la ruta sencera del fitxer: ")
    return ruta


def mostra_error_ruta_fitxer():
    print("No es troba cap fitxer en aquesta ruta.")
    print()
    demana_intro()
