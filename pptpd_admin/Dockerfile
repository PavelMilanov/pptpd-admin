FROM python:10

COPY . /
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD uvicorn main:app --host 0.0.0.0 --port 8000 --workers 2 --reload
