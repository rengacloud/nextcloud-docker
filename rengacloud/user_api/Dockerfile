FROM ubuntu:latest
MAINTAINER Alexander Ershov 'ershav@yandex.ru'
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip build-essential
COPY . /app
WORKDIR /app 
RUN pip install pipenv
RUN pipenv install --system
CMD ["python3", "server.py"]