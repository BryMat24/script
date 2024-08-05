# Base image
FROM python:3.10.5
# Installing prerequisite packages
RUN DEBIAN_FRONTEND="noninteractive" apt-get update && apt-get install -y tzdata
RUN apt-get -y install curl unzip groff less git

# Install Helm
RUN curl -o- "https://dl-cli.pstmn.io/install/linux64.sh" | sh

RUN mkdir /.postman && chmod -R 777 /.postman