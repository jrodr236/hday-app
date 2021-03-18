Instal·lació a Ubuntu a AWS
===========================

Accés via ssh sense clau pem:

https://forums.aws.amazon.com/message.jspa?messageID=878302

```bash
apt update
apt upgrade



apt install mariadb-server
mysql_secure_installation -> root password = AWS password
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

** pujar programa amb usuari hday **
chmod +x /home/hday/hday.sh

login hday

cd hday
pip3 install mysql-connector
cd
python3 hday/reiniciar.py


exit # tornar a ser root

nano /etc/ssh/sshd_config
Match User hday
       X11Forwarding no
       AllowTcpForwarding no
#       PermitTTY no
       ForceCommand ./hday.sh


systemctl restart sshd

./hday.sh


passwd ubuntu -> la mateixa que aws
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
