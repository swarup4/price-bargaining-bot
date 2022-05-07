# FROM ubuntu:18.04
# ENTRYPOINT []
# RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache rasa==2.5.2
# ADD . /app/
# RUN chmod +x /app/start_services.sh
# CMD /app/start_services.sh



FROM python:3.8.8 AS BASE

RUN apt-get update \
    && apt-get --assume-yes --no-install-recommends install \
        build-essential \
        curl \
        git \
        jq \
        libgomp1 \
        vim

WORKDIR /app

# upgrade pip version
RUN pip install --no-cache-dir --upgrade pip

RUN pip install rasa==2.5.2

ADD config.yml config.yml
ADD domain.yml domain.yml
ADD credentials.yml credentials.yml
ADD endpoints.yml endpoints.yml