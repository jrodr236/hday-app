# -*- coding: utf-8 -*-

"""
Dades de connexió amb l'SGBD
"""

from typing import Dict

from logica.claus import PASSWDBD

mysql_cfg: Dict[str, str] = {'host': 'localhost',
                             'user': 'hday',
                             'passwd': PASSWDBD,
                             'db': 'hday'}
