FROM ubuntu/postgres:14-22.04_beta

RUN apt-get update

RUN apt-get -y install gcc make cmake postgresql-server-dev-14 pip ca-certificates gnupg postgresql-14-postgis-3 postgis*

RUN pip install pgxnclient

RUN pgxn install h3

RUN mkdir script

ADD entrypoint/* /docker-entrypoint-initdb.d/

CMD ["postgres"]
