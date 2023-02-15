FROM python:3.9

WORKDIR /src
COPY requirements.txt /src
RUN pip insііtall -r requirements.txt
COPY . /src