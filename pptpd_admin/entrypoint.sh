#!/bin/bash

port=$1

apt install pptpd -y

set -e

cd app/ && uvicorn main:app --host 0.0.0.0 --port ${port} --workers 2 --reload
