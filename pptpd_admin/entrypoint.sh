#!/bin/bash

apt install pptpd -y

uvicorn main:app --host 0.0.0.0 --port 8000 --workers 2 --reload
