# -*- coding: utf-8 -*-

"""
Funcions de la capa de lògica de negoci de caràcter general
"""
from mysql.connector.errors import IntegrityError, DataError

from dades import usuari_dao
from logica.entitats import Usuari
from presentacio.errors import mostrar_error_usuari_ja_existeix_o_tipus_incorrecte, mostrar_error_verificar_usuari, \
    mostrar_error_format_dades
from presentacio.general import mostrar_capcalera, demanar_intro
from presentacio.usuari import existeix_usuari, demanar_login, demanar_registre


def demanar_usuari():
    """
    En iniciar l'aplicació, es demana l'usuari. Si existeix es fa login. Sino, es registra un nou usuari.
    :return: usuari que utilitzarà l'aplicació
    """
    mostrar_capcalera(None)
    usuari = None

    existeix = existeix_usuari()

    if existeix is None:
        # Si l'usuari no indica una opció vàlida, sortim
        return None

    if existeix:
        (nom, contrasenya) = demanar_login()
        usuari = usuari_dao.verificar(nom, contrasenya)
        if usuari is None:
            mostrar_error_verificar_usuari()
            demanar_intro()
        return usuari
    else:
        tipus_usuari = usuari_dao.obtenir_tipus_usuari()
        (nom, contrasenya, tipus) = demanar_registre(tipus_usuari)
        if nom is not None:
            usuari = Usuari(nom, contrasenya, tipus)
            try:
                usuari_dao.crear(usuari)
            except IntegrityError:
                mostrar_error_usuari_ja_existeix_o_tipus_incorrecte()
                demanar_intro()
                return None
            except DataError:
                mostrar_error_format_dades()
                demanar_intro()
                return None
    return usuari
