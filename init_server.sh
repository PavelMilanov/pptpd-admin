#!/usr/bin/bash

# install packages
apt update
apt install python3.8 curl -y

# install docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
rm get-docker.sh