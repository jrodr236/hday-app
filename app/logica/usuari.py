# -*- coding: utf-8 -*-

from mysql.connector.errors import IntegrityError, DataError

from dades import usuari_dao
from logica import constants
from logica.entitats import Usuari
from presentacio.errors import *
from presentacio.general import mostra_capcalera, demana_intro
from presentacio.usuari import demana_si_existeix_usuari, demana_login, demana_registre_de_nou_usuari


def demanar_usuari():
    mostra_capcalera(None)
    usuari = None

    existeix_usuari = demana_si_existeix_usuari()

    if existeix_usuari is None:
        # Si l'usuari no indica una opció vàlida, sortim
        return None

    if existeix_usuari:
        (nom, contrasenya) = demana_login()
        usuari = usuari_dao.autenticar(nom, contrasenya)
        if usuari is None:
            mostrar_error_verificar_usuari()
            demana_intro()
        return usuari
    else:
        tipus_usuari = usuari_dao.obtenir_els_tipus_usuari()
        tipus_usuari.remove(constants.TOTHOM)
        (nom, contrasenya, tipus) = demana_registre_de_nou_usuari(tipus_usuari)
        if tipus == constants.TOTHOM:
            mostrar_error_tipus_usuari_no_existeix()
            return None
        if nom is not None:
            usuari = Usuari(nom, contrasenya, tipus)
            try:
                usuari_dao.crear(usuari)
            except IntegrityError:
                mostrar_error_usuari_ja_existeix_o_tipus_incorrecte()
                demana_intro()
                return None
            except DataError:
                mostrar_error_format_dades()
                demana_intro()
                return None
    return usuari
