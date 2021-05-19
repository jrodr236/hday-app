Instal·lació a Ubuntu 20.04 a AWS
===========================

```bash
# Esdevenir root
sudo su -


# Actualitzar el sistema
apt update
apt upgrade


# Instal·lar MariaDB (bases de dades)
apt install mariadb-server
mysql_secure_installation -> root password = AWS password


# Instal·lar pip (gestor de paquets de python)
apt install python3-pip


# Crear la base de dades i l'usuari per accedir-hi
# Caldrà canviar ********** per una clau. Cal recordar-la perquè més endavant també es configurarà al fitxer logica/claus.py.

mysql -u root

CREATE DATABASE hday;
USE hday;
CREATE USER 'hday'@'localhost' IDENTIFIED BY '**********';
GRANT ALL PRIVILEGES ON * . * TO 'hday'@'localhost';
FLUSH PRIVILEGES;
EXIT


# Crear usuari del sistema que executarà l'aplicació i fer-hi login
/usr/sbin/adduser hday

login hday


# Descarregar l'aplicació.
wget https://github.com/jrodr236/hday-app/archive/refs/heads/master.zip
apt install unzip
unzip master.zip
mv hday-app-master/ hday-app/
chmod +x ~/hday-app/hday.sh


# Crear el fitxer logica/claus.py, a partir de exemple_claus.py
cd ~/hday-app/app/logica
cp exemple-claus.py claus.py


# Editar logica/claus.py i canviar les dues claus, tenint en compte el que s'indica en els comentaris d'aquest fitxer.
nano claus.py


# Instal·lar el coonnector de python-mysql
cd ~/hday-app
pip3 install mysql-connector


# Executar configuracions inicials de l'aplicació
python3 app/reiniciar.py


# Configurar el dimoni ssh per que s'executi l'aplicació directament en accedir via ssh
exit # tornar a ser root

nano /etc/ssh/sshd_config

# Afegir aquestes línies al final del fitxer
Match User hday
       X11Forwarding no
       AllowTcpForwarding no
#       PermitTTY no
       ForceCommand ./hday.sh


systemctl restart sshd


# Comprovar que l'aplicació funciona
login hday
cd hday-app
./hday.sh
```

---

Altres configuracions
---------------------

### Accedir via ssh sense clau pem

https://forums.aws.amazon.com/message.jspa?messageID=878302


### Canviar la configuració de la connexió a la base de dades

Aquesta configuració es troba al fitxer `dades/configuracio_db.py`

### Permetre connexions remotes a la base de dades

```bash
mysql -u root

USE hday;
CREATE USER 'hday-remote'@'%' IDENTIFIED BY '**********';
GRANT ALL PRIVILEGES ON * . * TO 'hday-remote'@'%';
FLUSH PRIVILEGES;
EXIT



a /etc/mysq/mariadb.conf.d/50-server.cnf, comentar línia:
#bind-address            = 127.0.0.1
```
