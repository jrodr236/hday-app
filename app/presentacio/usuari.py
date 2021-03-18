# -*- coding: utf-8 -*-

from getpass import getpass
from . import administracio
from .errors import mostrar_error_constrasenyes_no_coincideixen
from .general import demana_intro


def demana_si_existeix_usuari():
    te_usuari = input("Tens usuari? (S/N): ").lower()
    print()
    if te_usuari not in ["s", "n"]:
        print("Opció incorrecta.")
        demana_intro()
        return None
    else:
        return te_usuari == "s"


def demana_registre_de_nou_usuari(tipus_usuari):
    print("Si us plau, introdueix les credencials per al nou usuari.")
    print()
    nom = input("Nom: ")
    contrasenya = getpass("Contrasenya: ")
    contrasenya2 = getpass("Contrasenya (un altre cop): ")
    tipus = input("Tipus d'usuari " + formata_llista(tipus_usuari) + ": ").lower()
    print()
    if contrasenya != contrasenya2:
        mostrar_error_constrasenyes_no_coincideixen()
        demana_intro()
        return None, None, None
    return nom, contrasenya, tipus


def demana_login():
    print("Si us plau, introdueix les teves credencials.")
    print()
    nom = input("Nom: ")
    contrasenya = getpass("Contrasenya: ")
    print()
    return nom, contrasenya


def mostra_error_verificar_usuari():
    print("Usuari incorrecte.")
    print()


def formata_llista(llista):
    out = "("
    for item in llista:
        out = out + item + ", "
    out = out[0:-2] + ")"
    return out
