# -*- coding: utf-8 -*-


import mysql.connector

from .configuracio_db import mysql_cfg


def obtenir_connexio():
    conn = mysql.connector.connect(
        host=mysql_cfg['host'],
        user=mysql_cfg['user'],
        passwd=mysql_cfg['passwd'],
        database=mysql_cfg['db']
    )

    conn.autocommit = False

    return conn


def commit(conn, cursor):
    # https://pynative.com/python-mysql-transaction-management-using-commit-rollback/
    conn.commit()
    tancar_connexio(conn, cursor)


def tancar_connexio(conn, cursor):
    if conn.is_connected():
        cursor.close()
        conn.close()
