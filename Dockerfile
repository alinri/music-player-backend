FROM python:3.10.6-alpine

RUN apk update && \
    apk add --no-cache python3-dev py3-pip build-base mariadb-dev && \
    apk add --no-cache pkgconfig

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

COPY app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
