# -*- coding: utf-8 -*-

from mysql.connector.errors import IntegrityError, DataError

from dades import usuari_dao
from logica.entitats import Usuari
from presentacio.errors import *
from presentacio.general import mostrar_capcalera, demanar_intro
from presentacio.usuari import existeix_usuari, demanar_login, demanar_registre_de_nou_usuari


def demanar_usuari():
    mostrar_capcalera(None)
    usuari = None

    existeix = existeix_usuari()

    if existeix is None:
        # Si l'usuari no indica una opció vàlida, sortim
        return None

    if existeix:
        (nom, contrasenya) = demanar_login()
        usuari = usuari_dao.autenticar(nom, contrasenya)
        if usuari is None:
            mostrar_error_verificar_usuari()
            demanar_intro()
        return usuari
    else:
        tipus_usuari = usuari_dao.obtenir_tipus_usuari()
        (nom, contrasenya, tipus) = demanar_registre_de_nou_usuari(tipus_usuari)
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
