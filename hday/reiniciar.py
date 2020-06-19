#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Programa auxiliar per reiniciar l'aplicació.
Esborra i torna a crear les taules de la base de dades, i importa les proves i els reptes.
"""
from dades.administracio import eliminar_taules, crear_taules
from logica.administracio import importar_proves_csv

eliminar_taules()
crear_taules()

importar_proves_csv("michael.csv")
