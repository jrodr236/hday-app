# -*- coding: utf-8 -*-

from logica import constants
# L'encriptació de les contrasenyes es realitza al MySQL
from logica.claus import CLAU_PER_ENCRIPTAR_CONTRASENYES
from .helper import obtenir_connexio, commit


def eliminar_taules():
    conn = obtenir_connexio()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS Prova_superada")
    commit(conn, cursor)

    conn = obtenir_connexio()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS Usuari")
    commit(conn, cursor)

    conn = obtenir_connexio()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS Prova")
    commit(conn, cursor)

    conn = obtenir_connexio()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS Tipus_usuari")
    commit(conn, cursor)

    conn = obtenir_connexio()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS Repte")
    commit(conn, cursor)


def crear_taules():
    conn = obtenir_connexio()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE Repte (
            nom VARCHAR(40) NOT NULL,
            PRIMARY KEY (nom)
        )
    """)

    cursor.execute("""
        CREATE TABLE Tipus_usuari (
            tipus VARCHAR(20) NOT NULL,
            PRIMARY KEY (tipus)
        )
    """)

    cursor.execute("""
        CREATE TABLE Prova (
            repte VARCHAR(40) NOT NULL,
            ordre DECIMAL(2,0) NOT NULL,
            tipus_usuari VARCHAR(20) NOT NULL,
            enunciat VARCHAR(2048) NOT NULL,
            codi VARCHAR(30) NOT NULL,
            puntuacio DECIMAL(10,0) NOT NULL,
            PRIMARY KEY (repte, ordre),
            FOREIGN KEY (repte) REFERENCES Repte(nom)
                ON UPDATE CASCADE,
            FOREIGN KEY (tipus_usuari) REFERENCES Tipus_usuari(tipus)
                ON UPDATE CASCADE
        )
    """)

    cursor.execute("""
        CREATE TABLE Usuari (
            nom VARCHAR(10) NOT NULL,
            contrasenya BLOB NOT NULL,
            tipus VARCHAR(20) NOT NULL,
            PRIMARY KEY (nom),
            FOREIGN KEY (tipus) REFERENCES Tipus_usuari(tipus)
        )
    """)

    cursor.execute("""
        CREATE TABLE Prova_superada (
            data DATETIME,
            repte VARCHAR(40) NOT NULL,
            ordre_prova DECIMAL(2,0) NOT NULL,
            nom_usuari VARCHAR(10) NOT NULL,
            PRIMARY KEY (repte, ordre_prova, nom_usuari),
            FOREIGN KEY (repte, ordre_prova) REFERENCES Prova(repte, ordre)
                ON UPDATE CASCADE,
            FOREIGN KEY (nom_usuari) REFERENCES Usuari(nom)
                ON UPDATE CASCADE
        )
    """)

    query = """
            INSERT INTO Tipus_usuari(tipus)
            VALUES (%s)
        """
    cursor.executemany(query, [
        (constants.TOTHOM,),
        ("gm",),
        ("gs",)
    ])

    commit(conn, cursor)


def inserir_valors():
    conn = obtenir_connexio()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Repte(nom)
        VALUES  ("1r repte"),
                ("2n repte")
    """)

    cursor.execute("""
        INSERT INTO Prova(repte, ordre, tipus_usuari, enunciat, codi, puntuacio)
        VALUES  ("1r repte", 1, "tothom", "Enunciat prova 1", "codi 11", 100),
                ("1r repte", 2, "tothom", "Enunciat prova 2", "codi 12", 100),
                ("2n repte", 1, "tothom", "Enunciat prova 111", "codi 21", 100),
                ("2n repte", 2, "gm", "Enunciat prova 222", "codi 22", 1000),
                ("2n repte", 3, "gs", "Enunciat prova 333", "codi 33", 1000)
    """)

    query = """
        INSERT INTO Usuari(nom, contrasenya, tipus)
        VALUES  ("dummy1", AES_ENCRYPT(%s,UNHEX(%s)), "gm")
    """
    valors = ("patata", CLAU_PER_ENCRIPTAR_CONTRASENYES)
    cursor.execute(query, valors)

    query = """
        INSERT INTO Usuari(nom, contrasenya, tipus)
        VALUES  ("dummy2", AES_ENCRYPT(%s,UNHEX(%s)), "gs")
    """
    valors = ("patata", CLAU_PER_ENCRIPTAR_CONTRASENYES)
    cursor.execute(query, valors)

    cursor.execute("""
        INSERT INTO Prova_superada(data, repte, ordre_prova, nom_usuari)
        VALUES  ("2019-12-20 12:00:00", "1r repte", 1, "dummy1"),
                ("2019-12-20 12:01:00", "1r repte", 2, "dummy1"),
                ("2019-12-20 12:02:00", "2n repte", 1, "dummy1"),
                ("2019-12-20 12:03:00", "2n repte", 2, "dummy1")
    """)

    commit(conn, cursor)
