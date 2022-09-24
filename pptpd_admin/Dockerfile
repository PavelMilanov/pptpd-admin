FROM python:3.10

ARG PORT=8000

RUN apt update

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
EXPOSE ${PORT}
ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port ${PORT} --workers 2 --reload
