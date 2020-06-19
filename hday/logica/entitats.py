# -*- coding: utf-8 -*-

from hday.logica import constants


class Repte:

    def __init__(self, nom: str):
        self.nom = nom
        self.proves = []
        self.prova_per_superar = 0

    def afegeix_prova(self, prova):
        self.proves.append(prova)
        if prova.superada:
            self.prova_per_superar = self.prova_per_superar + 1

    def afegeix_proves(self, proves):
        self.prova_per_superar = 0
        self.proves = proves
        for p in proves:
            if p.superada:
                self.prova_per_superar = self.prova_per_superar + 1

    def dona_primera_prova_sense_resoldre(self):
        if self.esta_el_repte_superat():
            return None
        else:
            return self.proves[self.prova_per_superar]

    def esta_el_repte_superat(self) -> bool:
        return len(self.proves) == self.prova_per_superar


class Prova:

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
        self.superada = True
        self.repte.prova_per_superar = self.repte.prova_per_superar + 1


class ProvaSuperada:

    def __init__(self, data, prova, usuari):
        self.data = data
        self.prova = prova
        self.usuari = usuari


class Usuari:

    def __init__(self, nom: str, contrasenya: str, tipus: str):
        self.nom = nom
        self.contrasenya = contrasenya
        self.tipus = tipus
        self.punts = None

    def actualitzar_punts(self, punts: int):
        self.punts = punts

    def es_admin(self):
        return self.tipus == constants.ADMIN


class ProvaJaSuperada(Exception):
    pass
