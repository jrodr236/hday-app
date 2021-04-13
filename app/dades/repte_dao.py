# -*- coding: utf-8 -*-


from typing import List

from app.dades.helper import obtenir_connexio, commit
from app.dades.prova_dao import obtenir_proves_de_repte
from app.logica.entitats import Repte, Usuari


def obtenir_reptes_i_les_seves_proves(usuari: Usuari) -> List[Repte]:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
        SELECT (nom)
        FROM Repte
    """

    cursor.execute(query)

    resultat = cursor.fetchall()

    reptes = []

    commit(conn, cursor)

    for r in resultat:
        nom_repte = r[0]
        repte = Repte(nom_repte)
        obtenir_proves_de_repte(repte, usuari)
        reptes.append(repte)

    return reptes


def desar_reptes_i_les_seves_proves(reptes: List[Repte]) -> None:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    for repte in reptes:
        query = """
            INSERT IGNORE INTO Repte(nom)
            VALUES (%s)
        """
        valors = (repte.nom,)
        cursor.execute(query, valors)

        for prova in repte.proves:
            query = """
                INSERT INTO Prova(repte, ordre, tipus_usuari, enunciat, codi, puntuacio)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    enunciat=%s, codi=%s, puntuacio=%s
            """
            valors = (repte.nom, prova.ordre, None if prova.tipus_usuari == 'NULL' else prova.tipus_usuari,
                      prova.enunciat, prova.codi, prova.puntuacio,
                      prova.enunciat, prova.codi, prova.puntuacio)

            cursor.execute(query, valors)

    commit(conn, cursor)
