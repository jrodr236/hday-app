# -*- coding: utf-8 -*-

from presentacio.general import demana_intro


def demana_codi_per_superar_prova(repte):
    codi = ""
    if repte.esta_el_repte_superat():
        demana_intro()
    else:
        codi = input("Codi (ENTER per sortir): ")

    print()
    return codi


def mostra_avis_codi_correcte(codi_correcte):
    if codi_correcte:
        print("OK. Codi correcte.")
    else:
        print("ERROR. Codi incorrecte.")
    demana_intro()


def mostra_avis_prova_ja_superada():
    print("Aquesta prova ja havia estat superada.")
    print("ATENCIÓ: no facis trampes!")
    demana_intro()


def mostra_proves_per_superar_d_un_repte(repte):
    titol = "Repte: {}".format(repte.nom)
    print(titol)
    print("-" * len(titol))
    print()

    ordre_per_mostrar = 1
    for p in repte.proves:
        print("* Prova {} (#{}) *".format(ordre_per_mostrar, p.ordre))
        ordre_per_mostrar += 1
        print(p.enunciat)
        if p.superada:
            print("[PROVA SUPERADA]")
            print()
        else:
            # Prova no superada, no s'han d'ensenyar més
            break
