FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000