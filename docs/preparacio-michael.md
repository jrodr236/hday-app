
Repte inicial
=============

Prova 1
-------

Les màquines de cafè han cobrat vida! I ens ataquen!
Però com ens podem defensar d'aquestes màquines? Doncs treient-les l'electriciat.
En Michael, un antic fabricant de màquines de cafè, ens ha deixat una sèrie de pistes per trobar la localització del generador principal que fan servir les maleides màquines de cafè.
Aquesta és la primera pista:
192.168.7*2.7*2
ssh
michael/patata

### Resposta: 94873

### Puntuació: 100

### Preparació
#### Afegir usuari michael
adduser michael
> passwd patata

#### Protegir fitxers de michael
chown -R root:root /home/michael

#### Crear fitxer inicial
Afegim el següent al fitxer /home/michael/.profile:

> echo
> echo "CODI: 94873"


#### Configurar IP
ip address add 192.168.14.14 dev enp5s0


Prova 2
-------

look for the hidden file

### Resposta: 19433

### Puntuació: 100

### Preparació
Afegim el codi 19433 al fitxer .ocult.txt


Prova 3
-------

En Michael va esbrinar que una prova irrefutable que no ets una màquina de cafè és demostrar que ets capaç de fer malabars amb dues pilotes de paper durant 5 segons. Demostra-ho! Demostra que no ets una màquina de cafè!


### Resposta: 76328

### Puntuació: 100

### Preparació:
Escriure el codi 76328 en un paper, preparat per ensenyar-ho als alumnes que facin els malabars.


Prova 4
-------

Només podràn obtenir la ubicació del generador principal aquells que tinguin els nervis d'acer. Per demostrar-ho has de:
(Grau Mitjà) Grimpar un cable de xarxa seguint l'estandard TIA/EIA-568-B
(Grau Superior) Calcular la suma de tots els números senars que van del 99 al 999

### Resposta: 247599

### Puntuació: 200

### Preparació

```python
suma = 0
i = 99
while i <= 999:
    suma = suma + i
    i = i + 2

print(suma)
```