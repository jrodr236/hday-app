# -*- coding: utf-8 -*-


from typing import Dict

from app.logica.claus import CLAU_USUARI_BASE_DE_DADES

mysql_cfg: Dict[str, str] = {'host': 'localhost',
                             'user': 'hday',
                             'passwd': CLAU_USUARI_BASE_DE_DADES,
                             'db': 'hday'}
