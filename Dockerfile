FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install pip --upgrade \
    && pip install --no-cache-dir -r requirements.txt

COPY . /app

