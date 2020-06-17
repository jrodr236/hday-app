# -*- coding: utf-8 -*-

"""
Classes que representen les entitats principals de l'aplicació.
"""
from logica import constants


class Repte:
    """
    Entitat principal de l'aplicació. Un repte té vàries proves a superar.
    """

    def __init__(self, nom: str):
        self.nom = nom
        self.proves = []
        self.prova_per_superar = 0

    def afegeix_prova(self, prova):
        """
        Afegeix una sola prova al repte
        :param prova: prova a afegir
        """
        self.proves.append(prova)
        if prova.superada:
            self.prova_per_superar = self.prova_per_superar + 1

    def afegeix_proves(self, proves):
        """
        Afegeix totes les proves alhora.
        :param proves: conjunt de proves que s'afegeixen al repte.
        """
        self.prova_per_superar = 0
        self.proves = proves
        for p in proves:
            if p.superada:
                self.prova_per_superar = self.prova_per_superar + 1

    def dona_prova_sense_resoldre(self):
        """
        :return: la primera prova encara no resolta per l'usuari que juga
        """
        if self.repte_superat():
            return None
        else:
            return self.proves[self.prova_per_superar]

    def repte_superat(self) -> bool:
        """
        :return: True si totes les proves del repte han estat superades
        """
        return len(self.proves) == self.prova_per_superar


class Prova:
    """
    L'aplicació consisteix en anar superant proves.
    """

    def __init__(self, repte: Repte, ordre: int, tipus_usuari: str, enunciat: str, codi: str, puntuacio: int,
                 superada: bool = False):
        self.repte = repte
        #        repte.proves.append(self)
        self.ordre = ordre
        self.tipus_usuari = tipus_usuari
        self.enunciat = enunciat
        self.codi = codi
        self.puntuacio = puntuacio
        # Com que l'aplicació s'ha d'iniciar amb un sol usuari, l'atribut superada indica si aquest usuari que
        # juga ha superat la prova.
        self.superada = superada

    def superar(self):
        """
        S'ha de cridar a aquest mètode quan la prova ha estat superada.
        """
        self.superada = True
        self.repte.prova_per_superar = self.repte.prova_per_superar + 1


class ProvaSuperada:
    """
    Indica les proves que han estat superades per cada usuari.
    """

    def __init__(self, data, prova, usuari):
        self.data = data
        self.prova = prova
        self.usuari = usuari


class Usuari:
    """
    Classe que representa els usuaris de l'aplicació.
    """

    def __init__(self, nom: str, contrasenya: str, tipus: str):
        self.nom = nom
        self.contrasenya = contrasenya
        self.tipus = tipus
        self.punts = None

    def actualitzar_punts(self, punts: int):
        """
        Actualitza els punts acumulats de l'usuari
        :param punts: punts acumulats
        """
        self.punts = punts

    def es_admin(self):
        return self.tipus == constants.ADMIN


class ProvaJaSuperada(Exception):
    """
    Es llança quan s'intenta superar una prova que ja ha estat superada en un altre instància d'aquesta aplicació.
    """
    pass
