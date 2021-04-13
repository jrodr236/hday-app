# -*- coding: utf-8 -*-

from datetime import datetime

import mysql.connector

from app.dades.helper import obtenir_connexio, commit, tancar_connexio
from app.logica import constants
from app.logica.entitats import Repte, ProvaJaSuperada, Prova, Usuari


def verificar_codi(prova: Prova, usuari: Usuari, codi: str) -> bool:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
        SELECT *
        FROM Prova p
        WHERE p.repte=%s AND
            p.ordre = %s AND
            p.codi = %s
    """
    valors = (prova.repte.nom, prova.ordre, codi)
    cursor.execute(query, valors)

    resultat = cursor.fetchone()

    if resultat is None:
        return False
    ara = datetime.now()
    data_formatada = ara.strftime('%Y-%m-%d %H:%M:%S')
    sql = """
        INSERT INTO Prova_superada (data, repte, ordre_prova, nom_usuari)
        VALUES (%s, %s, %s, %s)
    """
    val = (data_formatada, prova.repte.nom, prova.ordre, usuari.nom)

    try:
        cursor.execute(sql, val)
        commit(conn, cursor)
        return True
    except mysql.connector.errors.IntegrityError:
        conn.rollback()
        tancar_connexio(conn, cursor)
        raise ProvaJaSuperada()


def obtenir_proves_de_repte(repte: Repte, usuari: Usuari) -> None:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
        SELECT ordre, tipus_usuari, enunciat, codi, puntuacio, ps.nom_usuari
        FROM Prova p
        LEFT JOIN Prova_superada ps ON
            p.repte = ps.repte AND
            p.ordre = ps.ordre_prova AND
            ps.nom_usuari = %s
        WHERE p.repte=%s
    """

    query += """
        AND p.tipus_usuari IN (%s, %s)
    """
    valors = (usuari.nom, repte.nom, usuari.tipus, constants.TOTHOM)

    query += """
        ORDER BY ordre
    """

    cursor.execute(query, valors)

    resultat = cursor.fetchall()

    proves = []

    for r in resultat:
        prova = Prova(repte, r[0], r[1], r[2], r[3], r[4], r[5] is not None)
        proves.append(prova)

    commit(conn, cursor)

    repte.afegeix_proves(proves)
