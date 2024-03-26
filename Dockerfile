FROM unit:1.32.0-python3.11

RUN apt-get update
RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential
RUN apt-get install -y pkg-config

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN rm requirements.txt

COPY app  /app
RUN chown -R unit:unit /app
COPY config.json /docker-entrypoint.d/config.json
# CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
