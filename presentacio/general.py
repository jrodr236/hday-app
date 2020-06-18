# -*- coding: utf-8 -*-

import os


def mostrar_menu_principal(admin):
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


def mostrar_reptes(reptes, permetre_crear_repte=False, mostrar_superats=False):
    print("Reptes")
    print("------")
    i = 1
    for r in reptes:
        info_superat = ""
        if mostrar_superats and r.esta_el_repte_superat():
            info_superat = " [REPTE SUPERAT]"
        print("{}. {}{}".format(i, r.nom, info_superat))
        i = i + 1
    if permetre_crear_repte:
        print("C. Crear nou repte")
    print("S. Sortir")
    print()


def escollir_repte(reptes, permetre_crear_repte=False):
    while True:
        seleccio = input("Escull el número de repte: ")
        print()

        if seleccio.lower() == "s":
            return "s"
        elif permetre_crear_repte and seleccio.lower() == "c":
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


def mostrar_capcalera(usuari_registrat=None, es_administrador=False):
    netejar_pantalla()
    print("  _                _    _                   _             ")
    print(" | |              | |  (_)                 | |            ")
    print(" | |__   __ _  ___| | ___ _ __   __ _    __| | __ _ _   _ ")
    print(" | '_ \\ / _` |/ __| |/ / | '_ \\ / _` |  / _` |/ _` | | | |")
    print(" | | | | (_| | (__|   <| | | | | (_| | | (_| | (_| | |_| |")
    print(" |_| |_|\\__,_|\\___|_|\\_\\_|_| |_|\\__, |  \\__,_|\\__,_|\\__, |")
    print("                                 __/ |               __/ |")

    if es_administrador:
        subtitulo = "[ ADMINISTRACIÓ ]"
    else:
        subtitulo = ""
        if usuari_registrat is not None:
            subtitulo = usuari_registrat.nom + " - " + str(usuari_registrat.punts) + " punts"

    print(subtitulo, end="")
    # for i in range(len(subtitulo), 32):
    print(" " * (32 - len(subtitulo)), end="")

    print("|___/               |___/ ")
    print()


def netejar_pantalla():
    os.system('clear')


def demanar_intro():
    input('Pressiona ENTER per continuar...')


def mostrar_accio_realitzada():
    print("Acció realitzada")
    print()
    demanar_intro()


def demanar_valor() -> str:
    valor = input("Introdueix el valor: ")
    print("")
    return valor
