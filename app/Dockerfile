FROM python:3.11
SHELL ["/bin/bash", "-c"]
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR .
RUN apt update && pip install --upgrade pip && mkdir "app"
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . .