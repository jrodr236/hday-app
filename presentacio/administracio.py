# -*- coding: utf-8 -*-

from .general import demanar_intro


def demanar_ruta_csv_per_importar_dades():
    print("El format de les files del fitxer per carregar les proves ha de ser:")
    print("nom prova,ordre,tipus_usuari(NULL/gm/gs),enunciat,codi,puntuacio")
    print()
    ruta = input("Introdueix la ruta sencera del fitxer: ")
    return ruta


def mostrar_error_ruta_fitxer():
    print("No es troba cap fitxer en aquesta ruta.")
    print()
    demanar_intro()


def formatar_llista(llista):
    out = "("
    for item in llista:
        out = out + item + ", "
    out = out[0:-2] + ")"
    return out
