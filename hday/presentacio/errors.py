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


def mostrar_error_repte_no_existeix():
    print("ERROR: no existeix el repte indicat.")


def mostrar_error_integritat_prova_superada():
    print("ERROR: error d'integritat. Pot ser que:")
    print("- Ja existeixi una Prova Superada per aquesta prova i usuari")
    print("- No existeixi algun dels elements associats (Repte, Prova o Usuari)")


def mostrar_error_prova_amb_superacions():
    print("ERROR: aquesta prova ha estat superada per algun usuari. És a dir, té proves superades associades.")


def mostrar_error_repte_amb_proves():
    print("ERROR: aquest repte té proves associades.")


def mostrar_error_tipus_usuari_no_existeix():
    print("ERROR: no existeix aquest tipus d'usuari.")


def mostrar_error_repte_ja_existeix():
    print("ERROR: ja existeix aquest repte.")