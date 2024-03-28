FROM python:3.10.6

RUN apt-get update
RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential
RUN apt-get install -y pkg-config

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN rm requirements.txt

COPY app  /app


CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
