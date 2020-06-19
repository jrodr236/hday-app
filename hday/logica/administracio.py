# -*- coding: utf-8 -*-


from mysql.connector.errors import IntegrityError, DataError

from dades import prova_dao, repte_dao, prova_superada_dao
from dades.administracio import *
from fitxers import *
from presentacio.administracio import *
from presentacio.errors import mostrar_error_lectura_fitxer, mostrar_error_format_dades, \
    mostrar_error_repte_no_existeix, mostrar_error_integritat_prova_superada, mostrar_error_repte_amb_proves, \
    mostrar_error_prova_amb_superacions, mostrar_error_tipus_usuari_no_existeix, mostrar_error_repte_ja_existeix
from presentacio.general import *


def administrar():
    """
    Funció principal d'administració de l'aplicació
    """
    while True:
        mostrar_capcalera(es_administrador=True)
        opcio = mostrar_menu_administracio()
        if opcio is None:
            continue
        elif opcio == "s":
            return

        executar = {
            "e": eliminar_taules,
            "c": crear_taules,
            "i": inserir_valors,
            "f": importar_proves_csv,
            "r": gestionar_reptes,
            "p": gestionar_proves,
            "o": gestionar_proves_superades,
            "u": gestionar_usuaris
        }
        executar[opcio]()

        if opcio in ["e", "c", "i"]:
            mostrar_accio_realitzada()


def importar_proves_csv(ruta=None):
    if ruta is None:
        ruta = demanar_ruta_csv_per_importar_dades()

    if not es_ruta_correcta(ruta):
        mostrar_error_ruta_fitxer()
        return

    try:
        reptes = llegir_fitxer_csv(ruta)
        repte_dao.desar_reptes_i_les_seves_proves(reptes)
        mostrar_accio_realitzada()
    except Exception as e:
        mostrar_error_lectura_fitxer(e)
        demanar_intro()


def gestionar_prova(prova):
    while True:
        mostrar_capcalera(es_administrador=True)
        opcio = mostrar_gestio_entitat(prova.repte.nom + " - Prova " + str(prova.ordre))

        if opcio == "m":
            mostrar_capcalera(es_administrador=True)
            mostrar_atributs_prova(prova)
        if opcio == "c":
            try:
                nom_repte_antic = prova.repte.nom
                ordre_antic = prova.ordre
                prova_nova = canviar_atributs_prova(prova)
                prova_dao.actualitzar(nom_repte_antic, ordre_antic, prova_nova)
                prova = prova_nova
            except DataError:
                mostrar_error_format_dades()
                demanar_intro()
            except IntegrityError:
                mostrar_error_repte_no_existeix()
                demanar_intro()
        elif opcio == "e":
            try:
                prova_dao.eliminar(prova)
                mostrar_accio_realitzada()
            except IntegrityError:
                mostrar_error_prova_amb_superacions()
                demanar_intro()
            break
        elif opcio == "s":
            return


def gestionar_prova_superada(prova_superada):
    while True:
        mostrar_capcalera(es_administrador=True)
        opcio = mostrar_gestio_entitat(prova_superada.prova.repte.nom + " - Prova " + str(prova_superada.prova.ordre) +
                                       ", " + prova_superada.usuari.nom)

        if opcio == "m":
            mostrar_capcalera(es_administrador=True)
            mostrar_atributs_prova_superada(prova_superada)
        if opcio == "c":
            try:
                nom_repte_antic = prova_superada.prova.repte.nom
                ordre_prova_antic = prova_superada.prova.ordre
                nom_usuari_antic = prova_superada.usuari.nom
                prova_superada_nova = canviar_atributs_prova_superada(prova_superada)
                prova_superada_dao.actualitzar(nom_repte_antic, ordre_prova_antic, nom_usuari_antic,
                                               prova_superada_nova)
                prova_superada = prova_superada_nova
            except DataError:
                mostrar_error_format_dades()
                demanar_intro()
            except IntegrityError:
                mostrar_error_integritat_prova_superada()
                demanar_intro()
        elif opcio == "e":
            prova_superada_dao.eliminar(prova_superada)
            mostrar_accio_realitzada()
            break
        elif opcio == "s":
            return


def crear_prova():
    try:
        prova = demanar_atributs_nova_prova()
        prova_dao.crear(prova)
        mostrar_accio_realitzada()
    except (DataError, ValueError):
        mostrar_error_format_dades()
        demanar_intro()
    except IntegrityError:
        mostrar_error_repte_no_existeix()
        demanar_intro()


def crear_prova_superada():
    try:
        prova_superada = demanar_atributs_nova_prova_superada()
        prova_superada_dao.crear(prova_superada)
        mostrar_accio_realitzada()
    except (DataError, ValueError):
        mostrar_error_format_dades()
        demanar_intro()
    except IntegrityError:
        mostrar_error_repte_no_existeix()
        demanar_intro()


def gestionar_proves():
    while True:
        mostrar_capcalera(es_administrador=True)
        proves = prova_dao.obtenir()
        mostrar_proves(proves, True, True)
        prova = escollir_prova(proves)
        if prova is None:
            continue
        elif prova == "s":
            return
        elif prova == "c":
            mostrar_capcalera(es_administrador=True)
            crear_prova()
        else:
            gestionar_prova(prova)


def gestionar_proves_superades():
    while True:
        mostrar_capcalera(es_administrador=True)
        proves_superades = prova_superada_dao.obtenir()
        mostrar_proves_superades(proves_superades)
        prova_superada = escollir_prova_superada(proves_superades)
        if prova_superada is None:
            continue
        elif prova_superada == "s":
            return
        elif prova_superada == "c":
            mostrar_capcalera(es_administrador=True)
            crear_prova_superada()
        else:
            gestionar_prova_superada(prova_superada)


def gestionar_repte(repte: Repte) -> None:
    while True:
        mostrar_capcalera(es_administrador=True)
        opcio = mostrar_gestio_entitat(repte.nom)

        if opcio == "m":
            mostrar_capcalera(es_administrador=True)
            mostrar_repte(repte)
        elif opcio == "c":
            try:
                nom_antic = repte.nom
                repte_nou = canviar_atributs_repte(repte)
                repte_dao.actualitzar(nom_antic, repte_nou)
                repte = repte_nou
                prova_dao.obtenir_proves_de_repte(repte)
            except DataError:
                mostrar_error_format_dades()
                demanar_intro()
            except IntegrityError:
                mostrar_error_repte_ja_existeix()
                demanar_intro()
        elif opcio == "e":
            try:
                repte_dao.eliminar(repte)
                mostrar_accio_realitzada()
            except IntegrityError:
                mostrar_error_repte_amb_proves()
                demanar_intro()
            break
        elif opcio == "s":
            return


def crear_repte():
    try:
        repte = demanar_atributs_nou_repte()
        repte_dao.crear(repte)
        mostrar_accio_realitzada()
    except (DataError, ValueError):
        mostrar_error_format_dades()
        demanar_intro()


def gestionar_reptes():
    while True:
        mostrar_capcalera(es_administrador=True)
        reptes = repte_dao.obtenir_reptes_i_les_seves_proves()
        mostrar_reptes(reptes, True)
        repte = escollir_repte(reptes, True)

        if repte is None:
            continue
        elif repte == "s":
            return
        elif repte == "c":
            mostrar_capcalera(es_administrador=True)
            crear_repte()
        else:
            gestionar_repte(repte)


def gestionar_usuaris():
    while True:
        mostrar_capcalera(es_administrador=True)
        usuaris = usuari_dao.obtenir()
        mostrar_usuaris(usuaris)
        usuari = escollir_usuari(usuaris)

        if usuari is None:
            continue
        elif usuari == "s":
            return
        elif usuari == "c":
            mostrar_capcalera(es_administrador=True)
            crear_usuari()
        else:
            gestionar_usuari(usuari)


def gestionar_usuari(usuari: Usuari) -> None:
    while True:
        mostrar_capcalera(es_administrador=True)
        opcio = mostrar_gestio_entitat(usuari.nom)

        if opcio == "m":
            mostrar_capcalera(es_administrador=True)
            mostrar_atributs_usuari(usuari)
        elif opcio == "c":
            try:
                nom_antic = usuari.nom
                llista_tipus_usuari = usuari_dao.obtenir_tipus_usuari()
                usuari_nou = canviar_atributs_usuari(usuari, llista_tipus_usuari)
                if usuari_nou is not None:
                    usuari_dao.actualitzar(nom_antic, usuari_nou)
                    usuari = usuari_nou
            except DataError:
                mostrar_error_format_dades()
                demanar_intro()
            except IntegrityError:
                mostrar_error_tipus_usuari_no_existeix()
                demanar_intro()
        elif opcio == "e":
            usuari_dao.eliminar(usuari)
            mostrar_accio_realitzada()
            break
        elif opcio == "s":
            return


def crear_usuari():
    try:
        tipus_usuari = usuari_dao.obtenir_tipus_usuari()
        usuari = demanar_atributs_nou_usuari(tipus_usuari)
        if usuari is not None:
            usuari_dao.crear(usuari)
            mostrar_accio_realitzada()
    except (DataError, ValueError):
        mostrar_error_format_dades()
        demanar_intro()
    except IntegrityError:
        mostrar_error_tipus_usuari_no_existeix()
        demanar_intro()
