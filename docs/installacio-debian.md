Instal·lació a Debian
=====================

```bash
apt install mariadb-server
mysql_secure_installation
apt install python3-pip



mysql -u root

CREATE DATABASE hday;
USE hday;
CREATE USER 'hday'@'localhost' IDENTIFIED BY '**********';
GRANT ALL PRIVILEGES ON * . * TO 'hday'@'localhost';
FLUSH PRIVILEGES;
EXIT

# La contrasenya utilitzada a ********** ha de configurar-se també al fitxer logica/claus.py 

/usr/sbin/adduser hday

** descarregar el programa amb usuari hday **
chmod +x /home/hday/hday-app/hday.sh

login hday

cd hday-app
pip3 install mysql-connector
python3 app/reiniciar.sh


exit # tornar a ser root

nano /etc/ssh/sshd_config
Match User hday
       X11Forwarding no
       AllowTcpForwarding no
#       PermitTTY no
       ForceCommand ./hday.sh


systemctl restart sshd

login hday
cd hday-app
./hday.sh
```

---

Permetre connexions remotes:

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
