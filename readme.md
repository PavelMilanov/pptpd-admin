## Веб-интерфейс для управления vpn-сервером
###  Технологии
- [Python3.10](https://www.python.org/downloads/ "Python3.10")
- [FastAPI](https://fastapi.tiangolo.com "FastAPI")
- [VueJS](https://v3.ru.vuejs.org/ "VueJS")
- [PPP-VPN](https://packages.debian.org/bullseye/pptpd "ppp-vpn")
- [Docker](https://docs.docker.com/engine/install/debian/ "Docker")

### Поддерживаемые ОС
	- Debian
	- Ubuntu

### Работа приложеня 
Приложение предоставляет веб-интерфейс для администрирования клиентских записей pptpd-vpn пакета для Debian дистрибутивов. Для корректной работы приложения необходима предварительная [настройка](/docs/configure_server.md) сервера. 

---

### Запуск приложения
1. ```cd /pptpd-admin```;
2. ```установить значения ARG p= и server_ip= в файле docker compose```;
3. ```docker compose up -d```;

![веб-интерфейс](/docs/web.png "Веб-интерфейс")

![swagger](/docs/swagger.png "Swagger")

---
