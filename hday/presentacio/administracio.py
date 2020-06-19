# -*- coding: utf-8 -*-

from typing import List

from dades import usuari_dao
from logica import constants
from logica.entitats import Prova, Repte, Usuari, ProvaSuperada
from .general import demanar_intro


def mostrar_menu_administracio():
    """
    Menú principal de l'administració
    :return: opció del menú escollida. None si la opció és incorrecta.
    """
    print("Menú d'administració")
    print("--------------------")
    print("E. Eliminar taules de la Base de Dades")
    print("C. Crear taules a la Base de Dades")
    print("I. Inserir dades de prova a la Base de Dades")
    print("F. Importar reptes i proves d'un fitxer CSV")
    print("R. Gestionar reptes")
    print("P. Gestionar proves")
    print("O. Gestionar proves superades")
    print("U. Gestionar usuaris")
    print("S. Sortir")
    print()

    opcio = input("Escull una opció: ").lower()
    print()

    if opcio not in ["e", "c", "i", "f", "r", "p", "o", "u", "s"]:
        print("Opció incorrecta.")
        demanar_intro()
        return None

    return opcio


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


def mostrar_gestio_entitat(identificador: str) -> str:
    print("Gestió d'una entitat ({})".format(identificador))
    print("---------------")
    print("M: Mostrar atributs")
    print("C: Canviar atributs")
    print("E: Eliminar")
    print("S: Sortir")
    print("")

    opcio = input("Escull una opció: ").lower()
    print()

    if opcio not in ["m", "c", "e", "s"]:
        print("Opció incorrecta.")
        demanar_intro()
        opcio = None

    return opcio


def mostrar_repte(repte: Repte):
    print("Atributs del repte")
    print("------------------")
    print("Nom: {}".format(repte.nom))
    print("Proves:")
    i = 1
    for p in repte.proves:
        print("{}. Prova {}".format(i, p.ordre))
        i = i + 1
    print("")
    demanar_intro()
    print("")


def canviar_atribut_de_entitat(nom_valor, valor_actual):
    print(nom_valor)
    print("Valor actual: {}".format(valor_actual))
    nou_valor = input("Nou valor (ENTER per no canviar): ")
    if nou_valor == "":
        nou_valor = valor_actual
    print("")
    return nou_valor


def canviar_atribut_de_entitat_amb_varies_linies(nom_valor, valor_actual):
    print(nom_valor)
    print("Valor actual:")
    print(valor_actual)
    print("Nou valor (No escriure res per no canviar, 2xENTER per finalitzar): ")

    nou_valor = ""
    stopword = ""
    while True:
        line = input()
        if line.strip() == stopword:
            nou_valor = nou_valor[0:-1]
            break
        nou_valor += "%s\n" % line

    if nou_valor == "":
        nou_valor = valor_actual
    # print("")
    return nou_valor


def canviar_atributs_repte(repte):
    print("Canviar atributs repte")
    print("----------------------")
    nom = canviar_atribut_de_entitat("Nom", repte.nom)
    return Repte(nom)


def canviar_atributs_usuari(usuari, tipus_usuari_existents):
    print("Canviar atributs usuari")
    print("----------------------.")
    nom = canviar_atribut_de_entitat("Nom", usuari.nom)
    contrasenya = canviar_atribut_de_entitat("Contrasenya, ", usuari.contrasenya)
    if usuari.contrasenya != contrasenya:
        # S'ha modificat la contrasenya. S'ha de tornar a demanar-la per seguretat
        contrasenya2 = input("Contrasenya (un altre cop): ")
        if contrasenya != contrasenya2:
            print("Les dues contrasenyes no coincideixen.")
            demanar_intro()
            return None
    tipus_usuari_existents.remove(constants.TOTHOM)
    tipus = canviar_atribut_de_entitat("Tipus {0}".format(formatar_llista(tipus_usuari_existents)), usuari.tipus).lower()
    if tipus == constants.TOTHOM:
        print("Tipus d'usuari incorrecte.")
        demanar_intro()
        return None
    usuari = Usuari(nom, contrasenya, tipus)
    return usuari


def mostrar_proves(proves: List[Prova], mostrar_repte=False, permetre_crear_repte=False):
    print("Proves")
    print("------")
    i = 1
    if mostrar_repte:
        for p in proves:
            print("{}. {} - Prova {}".format(i, p.repte.nom, p.ordre))
            i = i + 1
    else:
        for p in proves:
            print("{}. Prova {}".format(i, p.ordre))
            i = i + 1
    if permetre_crear_repte:
        print("C. Crear nova prova")
    print("S. Sortir")
    print()


def mostrar_proves_superades(proves_superades: List[ProvaSuperada]):
    print("Proves superades")
    print("----------------")
    i = 1
    for ps in proves_superades:
        print("{}. {}, prova {}, superada per {}".format(i, ps.prova.repte.nom, ps.prova.ordre, ps.usuari.nom))
        i = i + 1
    print("C. Crear nova prova")
    print("S. Sortir")
    print()


def mostrar_atributs_prova(prova):
    print("Atributs de la prova")
    print("--------------------")
    print("Repte: {}".format(prova.repte.nom))
    print("Ordre: {}".format(prova.ordre))
    print("Tipus usuari: {}".format(prova.tipus_usuari))
    print("Enunciat:")
    print(prova.enunciat)
    print("Codi: {}".format(prova.codi))
    print("Puntuacio: {}".format(prova.puntuacio))
    print("")
    demanar_intro()
    print("")


def mostrar_atributs_prova_superada(prova_superada):
    print("Atributs de la prova superada")
    print("-----------------------------")
    print("Data: {}".format(prova_superada.data))
    print("Repte: {}".format(prova_superada.prova.repte.nom))
    print("Ordre: {}".format(prova_superada.prova.ordre))
    print("Usuari: {}".format(prova_superada.usuari.nom))
    print("")
    demanar_intro()
    print("")


def escollir_prova(proves: List[Prova]):
    while True:
        seleccio = input("Escull el número de prova: ")
        print()

        if seleccio.lower() in ["s", "c"]:
            return seleccio.lower()

        if not seleccio.isdigit():
            print("Opció invàlida.")
            demanar_intro()
            return None

        numero = int(seleccio)
        if not (0 < numero <= len(proves)):
            print("Opció invàlida.")
            demanar_intro()
            return None

        numero = int(seleccio)
        prova_escollida = proves[numero - 1]
        # print("Repte escollit: {}.".format(repte_escollit.nom))
        # print()
        return prova_escollida


def escollir_prova_superada(proves_superades: List[ProvaSuperada]):
    while True:
        seleccio = input("Escull el número de prova superada: ")
        print()

        if seleccio.lower() in ["s", "c"]:
            return seleccio.lower()

        if not seleccio.isdigit():
            print("Opció invàlida.")
            demanar_intro()
            return None

        numero = int(seleccio)
        if not (0 < numero <= len(proves_superades)):
            print("Opció invàlida.")
            demanar_intro()
            return None

        numero = int(seleccio)
        prova_superada_escollida = proves_superades[numero - 1]
        return prova_superada_escollida


def demanar_atributs_nova_prova():
    print("Crear nova prova")
    print("---------------")
    print("Introdueix els atributs")
    nom_repte = input("Repte: ")
    ordre = input("Ordre: ")
    tipus_usuari = input(
        "Tipus usuari {0}: ".format(formatar_llista(usuari_dao.obtenir_tipus_usuari())))

    # enunciat = input("Enunciat: ")
    print("Enunciat (2xENTER per finalitzar):")
    enunciat = ""
    stopword = ""
    while True:
        line = input()
        if line.strip() == stopword:
            enunciat = enunciat[0:-1]
            break
        enunciat += "%s\n" % line

    codi = input("Codi: ")
    puntuacio = input("Puntuacio: ")
    prova = Prova(Repte(nom_repte), int(ordre), tipus_usuari, enunciat, codi, int(puntuacio))
    return prova


def demanar_atributs_nova_prova_superada():
    print("Crear nova prova superada")
    print("-------------------------")
    print("Introdueix els atributs")
    data = input("Data (any/mes/dia hora:minuts:segons): ")
    nom_repte = input("Repte: ")
    repte = Repte(nom_repte)
    ordre_prova = input("Ordre de la prova: ")
    prova = Prova(repte, int(ordre_prova), "", "", "", 0)
    nom_usuari = input("Usuari: ")
    usuari = Usuari(nom_usuari, "", "")
    prova_superada = ProvaSuperada(data, prova, usuari)
    return prova_superada


def demanar_atributs_nou_repte():
    print("Crear nou repte")
    print("---------------")
    print("Introdueix els atributs")
    nom = input("Nom: ")
    repte = Repte(nom)
    return repte


def demanar_atributs_nou_usuari(tipus_usuari):
    print("Crear nou usuari")
    print("----------------")
    print("Introdueix els atributs")
    nom = input("Nom: ")
    contrasenya = input("Contrasenya: ")
    contrasenya2 = input("Contrasenya (un altre cop): ")
    if contrasenya != contrasenya2:
        print("Les dues contrasenyes no coincideixen.")
        demanar_intro()
        return None

    tipus_usuari.remove(constants.TOTHOM)
    tipus = input("Tipus " + formatar_llista(tipus_usuari) + ": ").lower()

    if tipus == constants.TOTHOM:
        print("Tipus d'usuari incorrecte.")
        demanar_intro()
        return None

    usuari = Usuari(nom, contrasenya, tipus)
    return usuari


def formatar_llista(llista):
    out = "("
    for item in llista:
        out = out + item + ", "
    out = out[0:-2] + ")"
    return out


def canviar_atributs_prova(prova):
    print("Canviar atributs prova")
    print("----------------------")
    nom_repte = canviar_atribut_de_entitat("Repte", prova.repte.nom)
    repte = Repte(nom_repte)
    ordre = canviar_atribut_de_entitat("Ordre", prova.ordre)

    llista_tipus_usuari = usuari_dao.obtenir_tipus_usuari()
    tipus_usuari = canviar_atribut_de_entitat("Tipus usuari " + formatar_llista(llista_tipus_usuari), prova.tipus_usuari)

    enunciat = canviar_atribut_de_entitat_amb_varies_linies("Enunciat", prova.enunciat)
    codi = canviar_atribut_de_entitat("Codi", prova.codi)
    puntuacio = canviar_atribut_de_entitat("Puntuacio", prova.puntuacio)
    return Prova(repte, ordre, tipus_usuari, enunciat, codi, puntuacio)


def canviar_atributs_prova_superada(prova_superada):
    print("Canviar atributs prova superada")
    print("-------------------------------")
    data = canviar_atribut_de_entitat("Data (any/mes/dia hora:minuts:segons)", prova_superada.data)
    nom_repte = canviar_atribut_de_entitat("Repte", prova_superada.prova.repte.nom)
    repte = Repte(nom_repte)
    ordre = canviar_atribut_de_entitat("Ordre", prova_superada.prova.ordre)
    prova = Prova(repte, ordre, "", "", "", 0)
    nom_usuari = canviar_atribut_de_entitat("Usuari", prova_superada.usuari.nom)
    usuari = Usuari(nom_usuari, "", "")
    return ProvaSuperada(data, prova, usuari)


def mostrar_usuaris(usuaris: List[Usuari]):
    print("Usuaris")
    print("-------")
    i = 1
    for u in usuaris:
        print("{}. {}".format(i, u.nom))
        i = i + 1
    print("C. Crear nou usuari")
    print("S. Sortir")
    print()


def escollir_usuari(usuaris: List[Usuari]):
    while True:
        seleccio = input("Escull el número de l'usuari: ")
        print()

        if seleccio.lower() in ["s", "c"]:
            return seleccio.lower()

        if not seleccio.isdigit():
            print("Opció invàlida.")
            demanar_intro()
            return None

        numero = int(seleccio)
        if not (0 < numero <= len(usuaris)):
            print("Opció invàlida.")
            demanar_intro()
            return None

        numero = int(seleccio)
        usuari_escollit = usuaris[numero - 1]
        # print("Repte escollit: {}.".format(repte_escollit.nom))
        # print()
        return usuari_escollit


def mostrar_atributs_usuari(usuari):
    print("Atributs de l'usuari")
    print("--------------------")
    print("Nom: {}".format(usuari.nom))
    print("Contrasenya: {}".format(usuari.contrasenya))
    print("Tipus: {}".format(usuari.tipus))
    print("")
    demanar_intro()
    print("")
