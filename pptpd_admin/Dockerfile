FROM python:3.10

ARG p=8000
ENV PORT=${p}

RUN apt update

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port ${PORT} --workers 2 --reload
