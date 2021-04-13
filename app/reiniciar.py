#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app.dades.administracio import eliminar_taules, crear_taules
from app.logica.administracio import importar_proves_csv

eliminar_taules()
crear_taules()
importar_proves_csv("stan.csv")
