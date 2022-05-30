FROM debian:11

RUN apt update && apt install -y python3 python3-pip
COPY . /
RUN pip3 install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["bash", "entrypoint.sh"]
