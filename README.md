hday
====
Aplicació per gestionar l'event Hacking Day.

Aquest event és un joc que consisteix en superar una serie de proves.
Les proves estan organitzades en reptes.
Per superar cada prova s'ha d'indicar un codi correcte.


Arquitectura
============
L'arquitectura de l'aplicació és en capes:
- Presentació: interacció amb l'usuari
- Lògica (de negoci): nucli de l'aplicació.
- Dades + Fitxers: interacció amb el SGBD i els fitxers
  - Dins de la capa de DADES s'utilitza el patró DAO
  
Per cadascuna de les capes hi ha un mòdul amb el nom adient.

Per simplificar, la verificació de les dades la realitzarà l'SBGD.

Instal·lació i configuració
===========================

* [debian](docs/installacio-debian.md)
* [ubuntu + AWS](docs/installacio-ubuntu-aws.md)


