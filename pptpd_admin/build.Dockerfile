FROM debian:11

ARG p=8000
ENV PORT=$p

RUN apt update && apt install -y python3 python3-pip
COPY . /app
RUN pip3 install -r app/requirements.txt
EXPOSE ${PORT}
ENTRYPOINT bash app/entrypoint.sh ${PORT}
