Repte inicial
=============

Prova 1
-------

"Les màquines de cafè han cobrat vida! I ens ataquen!
Però com ens podem defensar d'aquestes màquines? Doncs treient-les l'electriciat.
L'Stan, un antic fabricant de màquines de cafè, ens ha deixat una sèrie de pistes per trobar la localització del generador principal que fan servir les maleides màquines de cafè.
Aquesta és la primera pista:
IP-STAN1
22
stan
patata"

### Resposta: 94873

### Puntuació: 100

### Preparació
#### Afegir usuari michael
adduser stan
> passwd patata

#### Protegir fitxers de michael
chown -R root:root /home/stan

#### Creem directori i fitxer
cd /home/stan
mkdir .secret
cd .secret
nano .ocult
>>>> 54853



Prova 2
-------

L'Stan es va adonar que alguna cosa no anava bé el dia que va aparèixer un café a la serie Game of Thrones. Molta gent se'n va adonar, es va fer viral, però la intel·ligència aritificial col·lectiva lligada a les màquines de café van eliminar la prova. I per dissimular van fer dir a l'actriu que es tractava de té. Quin és el nom d'aquesta actriu?

### Resposta: Emilia Clarke

### Puntuació: 100

### Preparació



Prova 3
-------

"L'Stan va esbrinar que una prova irrefutable que no ets una màquina de cafè és demostrar que ets capaç de fer malabars amb dues pilotes de paper durant 5 segons. Demostra-ho! Demostra que no ets una màquina de cafè!
Un cop fets els malabars, escriu el codi 85715."


### Resposta: 76328

### Puntuació: 100

### Preparació:
RES


Prova 4 (gm)
-------

Només podràn obtenir la ubicació del generador principal aquells que tinguin un coneixement profund de la història de les màquines de cafè. Per demostrar-ho, indica l'any que es va fundar Nespresso

### Resposta
1986


Prova 5 (gs)
------------

Només podràn obtenir la ubicació del generador principal aquells que tinguin els nervis d'acer. Per demostrar-ho has de calcular quants números hi ha entre l'1 i el 10000 que la suma dels seus dígits acabi en 3.

```python
def suma_digits(numEntero):
    sumDigit=0
    while numEntero != 0:
        extNum = numEntero % 10
        numEntero //= 10
        sumDigit += extNum
    return sumDigit

quantitat = 0
numero = 1
while numero <= 10000:
    suma = suma_digits(numero)
    if suma%10 == 3:
        quantitat += 1
    numero += 1

print(quantitat)
```

### Resposta
1000