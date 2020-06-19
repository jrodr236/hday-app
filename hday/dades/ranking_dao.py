# -*- coding: utf-8 -*-

"""
No hi ha taula Ranking, però es pot obtenir a partir de JOINs entre diverses taules.
"""

from typing import List
from dades.helper import obtenir_connexio, commit


def obtenir() -> List:
    conn = obtenir_connexio()

    cursor = conn.cursor()

    query = """
        SELECT ps.nom_usuari, u.tipus, SUM(p.puntuacio), MAX(ps.data)
        FROM Prova_superada ps, Prova p, Usuari u
        WHERE ps.repte=p.repte AND
            ps.ordre_prova = p.ordre AND
            ps.nom_usuari = u.nom
        GROUP BY ps.nom_usuari
        ORDER BY SUM(p.puntuacio) DESC, MAX(ps.data)
        LIMIT 15
    """
    # valors = (usuari.nom, )
    cursor.execute(query)  # , valors)

    ranking = []
    resultat = cursor.fetchall()
    for r in resultat:
        ranking.append((r[0], r[1], r[2], r[3]))

    commit(conn, cursor)
    return ranking
