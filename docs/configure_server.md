## Предварительная настройка сервера
1. Установка необходимых пакетов
	`apt update && apt install pptpd nfttables -y`
2. Отредактировать `/etc/pptpd.conf` файл 
	```
	# (Recommended)
	#localip 192.168.0.1
	#remoteip 192.168.0.234-238,192.168.0.245
	```
	```
	# (Recommended)
	localip 10.0.0.1
	remoteip 10.0.0.100-200
	```
3. Отредактировать  `/etc/ppp/pptpd-options` файл 
	```
	#ms-dns 192.168.0.1
	#ms-dns 192.168.0.2
	```
	```
	ms-dns 77.88.8.1  / ваш dns
	ms-dns 77.88.8.8  / ваш dns
	```
4. Включить маршрутизацию трафика между интерфейсами
	`cd /etc/sysctl.conf`
	`net.ipv4.ip_forward=1`
5.  Перезагрузить сервер или выполнить команду
        `echo 1 > /proc/sys/net/ipv4/ip_forward`
6. Включить службу vpn-сервера
	`systemctl enable pptpd`
	`systemctl start pptpd`
7. Настройка NAT
	```
	nft add table ip nat
	nft add chain nat POSTROUTING { type nat hook postrouting priority 0\; }
	nft add rule ip nat POSTROUTING ip saddr 10.0.0.0/24 oifname <интерфейс во внешней сети> counter masquerade
	```
8. Запустить [веб-приложение](../readme.md)