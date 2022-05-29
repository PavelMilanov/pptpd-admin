FROM debian:11

RUN apt update && apt install -y python3 python3-pip pptpd
COPY . /
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD uvicorn main:app --host 0.0.0.0 --port 8000 --workers 2 --reload
