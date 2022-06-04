FROM debian:11

RUN apt update && apt install -y python3 python3-pip
COPY . /app
RUN pip3 install -r app/requirements.txt
EXPOSE 8000
ENTRYPOINT ["bash", "app/entrypoint.sh"]
