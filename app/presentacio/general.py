# -*- coding: utf-8 -*-

import os


def mostra_menu_principal():
    print("Menú principal")
    print("--------------")
    print("J. Jugar")
    print("R. Ranking")
    print("E. Esdeveniments")
    print("S. Sortir")
    print()

    opcio = input("Escull una opció: ").lower()
    print()

    if not (opcio in ["j", "e", "r", "s"]):
        print("Opció incorrecta.")
        demana_intro()
        opcio = None

    return opcio


def mostra_reptes(reptes):
    print("Reptes")
    print("------")
    i = 1
    for r in reptes:
        info_superat = ""
        if r.esta_el_repte_superat():
            info_superat = " [REPTE SUPERAT]"
        print("{}. {}{}".format(i, r.nom, info_superat))
        i = i + 1
    print("S. Sortir")
    print()


def escull_repte(reptes, permetre_crear_repte=False):
    while True:
        seleccio = input("Escull el número de repte: ")
        print()

        if seleccio.lower() == "s":
            return "s"

        if not seleccio.isdigit():
            print("Opció invàlida.")
            demana_intro()
            return None

        numero = int(seleccio)
        if not (0 < numero <= len(reptes)):
            print("Opció invàlida.")
            demana_intro()
            return None

        numero = int(seleccio)
        repte_escollit = reptes[numero - 1]
        return repte_escollit


def mostra_capcalera(usuari_registrat=None):
    neteja_pantalla()
    print("  _                _    _                   _             ")
    print(" | |              | |  (_)                 | |            ")
    print(" | |__   __ _  ___| | ___ _ __   __ _    __| | __ _ _   _ ")
    print(" | '_ \\ / _` |/ __| |/ / | '_ \\ / _` |  / _` |/ _` | | | |")
    print(" | | | | (_| | (__|   <| | | | | (_| | | (_| | (_| | |_| |")
    print(" |_| |_|\\__,_|\\___|_|\\_\\_|_| |_|\\__, |  \\__,_|\\__,_|\\__, |")
    print("                                 __/ |               __/ |")

    subtitol = ""
    if usuari_registrat is not None:
        subtitol = usuari_registrat.nom + " - " + str(usuari_registrat.punts) + " punts"

    print(subtitol, end="")
    print(" " * (32 - len(subtitol)), end="")

    print("|___/               |___/ ")
    print()


def neteja_pantalla():
    os.system('clear')


def demana_intro():
    input('Pressiona ENTER per continuar...')


def mostra_accio_realitzada():
    print("Acció realitzada")
    print()
    demana_intro()
