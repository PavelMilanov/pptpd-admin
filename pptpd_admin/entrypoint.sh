#!/bin/bash

apt install pptpd -y

cd app/ && uvicorn main:app --host 0.0.0.0 --port 8000 --workers 2 --reload
