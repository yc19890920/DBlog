# pull official base image
# pull official base image
# FROM python:2.7.15-alpine
FROM python:2.7.15

# set work directory
WORKDIR /app

# set environment variables
# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install MySQL-python dependencies
#RUN apt-get install libmysqlclient-dev default-libmysqlclient-dev
RUN apt-get update && apt-get -y install python mysql-server python-mysqldb
#RUN set -ex && apk --no-cache add --virtual build-dependencies  build-base py-mysqldb gcc libc-dev libffi-dev mariadb-dev
# && pip install --no-cache-dir mysql-python

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /app/entrypoint.sh

# copy project
COPY . /app

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
