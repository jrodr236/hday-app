# -*- coding: utf-8 -*-


def mostrar_error_usuari_ja_existeix_o_tipus_incorrecte():
    print("ERROR: Ja existeix aquest usuari, o tipus d'usuari incorrecte.")


def mostrar_error_control_c():
    print()
    print()
    print("Si us plau, utilitza els menús per sortir de l'aplicació amb normalitat.")


def mostrar_error_verificar_usuari():
    print("ERROR: no existeix aquest usuari/contrasenya.")


def mostrar_error_lectura_fitxer(e: Exception):
    print("ERROR: hi ha hagut algun problema amb la lectura del fitxer.")
    print("Detalls: {}".format(e))


def mostrar_error_format_dades():
    print("ERROR: format de dades incorrecte.")


def mostrar_error_tipus_usuari_no_existeix():
    print("ERROR: no existeix aquest tipus d'usuari.")
