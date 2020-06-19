# -*- coding: utf-8 -*-

from typing import List

from hday.logica.claus import CLAU_CONTRASENYA
from hday.logica.entitats import Usuari
from hday.dades.helper import obtenir_connexio, commit


def crear(usuari: Usuari) -> None:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
        INSERT INTO Usuari(nom, contrasenya, tipus)
        VALUES (%s, AES_ENCRYPT(%s,UNHEX(%s)), %s)
    """
    valors = (usuari.nom, usuari.contrasenya, CLAU_CONTRASENYA, usuari.tipus)

    cursor.execute(query, valors)

    commit(conn, cursor)


def autenticar(nom, contrasenya):
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
        SELECT tipus
        FROM Usuari
        WHERE nom=%s AND contrasenya=AES_ENCRYPT(%s, UNHEX(%s))
    """
    valors = (nom, contrasenya, CLAU_CONTRASENYA)
    cursor.execute(query, valors)

    resultat = cursor.fetchone()

    commit(conn, cursor)
    if resultat is not None:
        return Usuari(nom, contrasenya, resultat[0])
    else:
        return None


def obtenir_punts(usuari: Usuari) -> None:
    conn = obtenir_connexio()
    cursor = conn.cursor()

    query = """
        SELECT SUM(puntuacio)
        FROM Prova_superada ps, Prova p
        WHERE ps.repte=p.repte AND
            ps.ordre_prova = p.ordre AND
            nom_usuari = %s;
    """
    valors = (usuari.nom,)
    cursor.execute(query, valors)

    puntuacio = 0
    resultat = cursor.fetchone()
    if resultat[0] is not None:
        puntuacio = resultat[0]

    commit(conn, cursor)

    usuari.actualitzar_punts(puntuacio)


def obtenir() -> List[Usuari]:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
        SELECT nom, AES_DECRYPT(contrasenya, UNHEX(%s)), tipus
        FROM Usuari
    """
    valors = (CLAU_CONTRASENYA,)

    cursor.execute(query, valors)

    resultat = cursor.fetchall()

    usuaris = []

    for r in resultat:
        usuari = Usuari(r[0], r[1].decode("utf-8"), r[2])
        usuaris.append(usuari)

    commit(conn, cursor)

    return usuaris


def actualitzar(nom_antic: str, usuari: Usuari) -> None:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
            UPDATE Usuari
            SET nom = %s,
                contrasenya = AES_ENCRYPT(%s, UNHEX(%s)),
                tipus = %s
            WHERE nom = %s
        """
    valors = (usuari.nom, usuari.contrasenya, CLAU_CONTRASENYA, usuari.tipus, nom_antic)
    cursor.execute(query, valors)

    commit(conn, cursor)


def eliminar(usuari: Usuari) -> None:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
            DELETE FROM Usuari
            WHERE nom = %s
        """
    valors = (usuari.nom,)
    cursor.execute(query, valors)

    commit(conn, cursor)


def obtenir_tipus_usuari():
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
        SELECT tipus
        FROM Tipus_usuari
    """

    cursor.execute(query)

    resultat = cursor.fetchall()

    tipus = []

    for r in resultat:
        tipus.append(r[0])

    commit(conn, cursor)

    return tipus


