# -*- coding: utf-8 -*-

from app.dades.helper import obtenir_connexio, commit
from app.logica.claus import CLAU_PER_ENCRIPTAR_CONTRASENYES
from app.logica.entitats import Usuari


def crear(usuari: Usuari) -> None:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
        INSERT INTO Usuari(nom, contrasenya, tipus)
        VALUES (%s, AES_ENCRYPT(%s,UNHEX(%s)), %s)
    """
    valors = (usuari.nom, usuari.contrasenya, CLAU_PER_ENCRIPTAR_CONTRASENYES, usuari.tipus)

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
    valors = (nom, contrasenya, CLAU_PER_ENCRIPTAR_CONTRASENYES)
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


def obtenir_els_tipus_usuari():
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
