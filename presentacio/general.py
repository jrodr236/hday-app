# -*- coding: utf-8 -*-

"""
Funcions generals de la capa de presentació.
"""

import os


def mostrar_menu_principal(admin):
    """
    Menú principal de l'aplicació
    :param admin: True si l'usuari que ha fet login és administrador
    :return: opció escollida al menú
    """
    print("Menú principal")
    print("--------------")
    if admin:
        print("A. Administrar")
    else:
        print("J. Jugar")
    print("R. Ranking")
    print("E. Esdeveniments")
    print("S. Sortir")
    print()

    opcio = input("Escull una opció: ").lower()
    print()

    if not (opcio in ["j", "e", "r", "s"] or (opcio == "a" and admin)):
        print("Opció incorrecta.")
        demanar_intro()
        opcio = None

    return opcio


def mostrar_reptes(reptes, crear=False, mostrar_superats=False):
    """
    Mostra un llistat dels Reptes
    :param reptes: llistat dels reptes a mostrar
    :param crear: True si s'ha de mostrar una opció per crear un repte
    :param mostrar_superats: True si s'han de mostrar els reptes superats
    """
    print("Reptes")
    print("------")
    i = 1
    for r in reptes:
        info_superat = ""
        if mostrar_superats and r.repte_superat():
            info_superat = " [REPTE SUPERAT]"
        print("{}. {}{}".format(i, r.nom, info_superat))
        i = i + 1
    if crear:
        print("C. Crear nou repte")
    print("S. Sortir")
    print()


def escollir_repte(reptes, crear=False):
    """
    Permet escollir un repte
    :param reptes: conjunt de reptes dels que se'n pot escollir un
    :param crear: True si s'ha de tenir en compte la opció de crear un nou repte
    :return: el repte escollit
    """
    while True:
        seleccio = input("Escull el número de repte: ")
        print()

        if seleccio.lower() == "s":
            return "s"
        elif crear and seleccio.lower() == "c":
            return "c"

        if not seleccio.isdigit():
            print("Opció invàlida.")
            demanar_intro()
            return None

        numero = int(seleccio)
        if not (0 < numero <= len(reptes)):
            print("Opció invàlida.")
            demanar_intro()
            return None

        numero = int(seleccio)
        repte_escollit = reptes[numero - 1]
        return repte_escollit


def mostrar_capcalera(usuari=None, admin=False):
    """
    Capçalera de l'aplicació
    :param usuari: usuari que s'ha registrat a l'aplicació. Si és None, és que encara no s'ha registrat cap usuari.
    :param admin: True si la capçalera és per l'administració de l'aplicació
    :return:
    """
    netejar_pantalla()
    print("  _                _    _                   _             ")
    print(" | |              | |  (_)                 | |            ")
    print(" | |__   __ _  ___| | ___ _ __   __ _    __| | __ _ _   _ ")
    print(" | '_ \\ / _` |/ __| |/ / | '_ \\ / _` |  / _` |/ _` | | | |")
    print(" | | | | (_| | (__|   <| | | | | (_| | | (_| | (_| | |_| |")
    print(" |_| |_|\\__,_|\\___|_|\\_\\_|_| |_|\\__, |  \\__,_|\\__,_|\\__, |")
    print("                                 __/ |               __/ |")

    if admin:
        subtitulo = "[ ADMINISTRACIÓ ]"
    else:
        subtitulo = ""
        if usuari is not None:
            subtitulo = usuari.nom + " - " + str(usuari.punts) + " punts"

    print(subtitulo, end="")
    # for i in range(len(subtitulo), 32):
    print(" " * (32 - len(subtitulo)), end="")

    print("|___/               |___/ ")
    print()


def netejar_pantalla():
    """
    Neteja la pantalla
    """
    os.system('clear')


def demanar_intro():
    """
    Demana que s'introdueixi ENTER per permetre a l'usuari llegir la pantalla
    """
    input('Pressiona ENTER per continuar...')


def mostrar_accio_realitzada():
    """
    Mostra un missatge que indica que una acció s'ha realitzat
    :return:
    """
    print("Acció realitzada")
    print()
    demanar_intro()


def demanar_valor() -> str:
    """
    Demana que s'introdueixi un valor
    :return:
    """
    valor = input("Introdueix el valor: ")
    print("")
    return valor
