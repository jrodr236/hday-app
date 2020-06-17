from typing import List

from dades.helper import obtenir_connexio, commit
from logica import constants
from logica.entitats import Usuari, Repte, Prova, ProvaSuperada


def obtenir() -> List:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
        SELECT data, nom_usuari, contrasenya, tipus, ps.repte, ordre_prova, enunciat, codi, p.puntuacio
        FROM Prova_superada ps, Prova p, Usuari u
        WHERE ps.repte = p.repte AND
            ps.ordre_prova = p.ordre AND
            ps.nom_usuari = u.nom
        ORDER BY data DESC
        LIMIT 15
    """
    cursor.execute(query)

    resultat = cursor.fetchall()

    usuaris = []
    reptes = []
    proves = []
    proves_superades = []

    for r in resultat:
        data = r[0]
        nom_usuari = r[1]
        contrasenya = r[2]
        tipus = r[3]
        usuari = next((x for x in usuaris if x.nom == nom_usuari), None)
        if usuari is None:
            usuari = Usuari(nom_usuari, contrasenya, tipus)
            usuaris.append(usuari)

        nom_repte = r[4]
        repte = next((x for x in reptes if x.nom == nom_repte), None)
        if repte is None:
            repte = Repte(nom_repte)
            reptes.append(repte)

        ordre_prova = r[5]
        enunciat = r[6]
        codi = r[7]
        puntuacio = r[8]
        prova = next((x for x in proves if x.repte.nom == nom_repte and x.ordre == ordre_prova), None)
        if prova is None:
            prova = Prova(repte, ordre_prova, "", enunciat, codi, puntuacio)
            proves.append(prova)

        prova_superada = ProvaSuperada(data, prova, usuari)
        proves_superades.append(prova_superada)

    commit(conn, cursor)

    return proves_superades


def crear(prova_superada: ProvaSuperada):
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
            INSERT INTO Prova_superada (data, repte, ordre_prova, nom_usuari)
            VALUES (%s, %s, %s, %s)
        """
    valors = (prova_superada.data, prova_superada.prova.repte.nom, prova_superada.prova.ordre,
              prova_superada.usuari.nom)
    cursor.execute(query, valors)

    commit(conn, cursor)


def actualitzar(nom_repte_antic: str, ordre_prova_antic: int, nom_usuari_antic: str,
                prova_superada_nova: ProvaSuperada) -> None:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
            UPDATE Prova_superada
            SET data = %s,
                repte = %s,
                ordre_prova = %s,
                nom_usuari = %s
            WHERE repte = %s AND
                ordre_prova = %s AND
                nom_usuari = %s
        """
    valors = (prova_superada_nova.data,
              prova_superada_nova.prova.repte.nom,
              prova_superada_nova.prova.ordre,
              prova_superada_nova.usuari.nom,
              nom_repte_antic,
              ordre_prova_antic,
              nom_usuari_antic)
    cursor.execute(query, valors)

    commit(conn, cursor)


def eliminar(prova_superada: ProvaSuperada):
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
            DELETE FROM Prova_superada
            WHERE repte = %s AND
                ordre_prova = %s AND
                nom_usuari = %s
        """
    valors = (prova_superada.prova.repte.nom,
              prova_superada.prova.ordre,
              prova_superada.usuari.nom)
    cursor.execute(query, valors)

    commit(conn, cursor)
