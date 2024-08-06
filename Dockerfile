# Base image
FROM python:3.10.5
# Installing prerequisite packages
RUN DEBIAN_FRONTEND="noninteractive" apt-get update && apt-get install -y tzdata
RUN apt-get -y install curl unzip groff less git

COPY requirements.txt .

RUN pip install --upgrade pip==24.0
RUN pip install -r requirements.txt