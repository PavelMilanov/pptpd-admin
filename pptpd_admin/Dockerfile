FROM python:3.10

RUN apt update

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
EXPOSE 8000
ENTRYPOINT bash entrypoint.sh
