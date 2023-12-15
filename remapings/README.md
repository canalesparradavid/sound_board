# Remapeo

### Entorno visual (con GUI)
remapeo: xmodmap</br>
deteccion teclas: xev

### Entorno sin GUI
remapeo: loadkeys</br>
deteccion teclas: showkeys

[configurar raspberry](https://raspberrypi.stackexchange.com/questions/2169/how-do-i-force-the-raspberry-pi-to-turn-on-hdmi#:~:text=hdmi_force_hotplug%3D1%20sets%20the%20Raspbmc,no%20audio\)%20mode%20by%20default.)

```
hdmi_force_hotplug=1
hdmi_drive=2
```

boot in console autologued in


### Cambio configuracion
[Tutorial FTP](https://linuxconfig.org/how-to-setup-and-use-ftp-server-in-ubuntu-linux)

```
sudo apt install vsftpd
sudo mv /etc/vsftpd.conf /etc/vsftpd.conf_orig

sudo nano /etc/vsftpd.conf
```

```
listen=NO
listen_ipv6=YES
anonymous_enable=NO
local_enable=YES
write_enable=YES
local_umask=022
dirmessage_enable=YES
use_localtime=YES
xferlog_enable=YES
connect_from_port_20=YES
chroot_local_user=YES
secure_chroot_dir=/var/run/vsftpd/empty
pam_service_name=vsftpd
rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
ssl_enable=NO
pasv_enable=Yes
pasv_min_port=10000
pasv_max_port=10100
allow_writeable_chroot=YES
```

CTRL-O
CTRL-X

```
sudo ufw allow from any to any port 20,21,10000:10100 proto tcp [IGUAL NO NECESARIO]
sudo systemctl restart vsftpd
```

```
[OPCIONAL]
sudo useradd -m ftpuser
sudo passwd ftpuser
```
