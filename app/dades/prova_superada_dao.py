# -*- coding: utf-8 -*-

from typing import List
from dades.helper import obtenir_connexio, commit
from logica import constants
from logica.entitats import Usuari, Repte, Prova, ProvaSuperada


def obtenir_proves() -> List:
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
