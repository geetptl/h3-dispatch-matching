FROM ubuntu/postgres:14-22.04_beta

RUN apt-get update

RUN apt-get -y install gcc make cmake postgresql-server-dev-14 pip ca-certificates gnupg postgresql-14-postgis-3 postgis*

RUN pip install pgxnclient

RUN pgxn install h3

RUN mkdir script

RUN echo 'psql -U username -d db -c "create extension postgis;" -c "create extension postgis_raster;" -c "create extension postgis_topology;"' > /docker-entrypoint-initdb.d/01-gis_extensions.sh

RUN echo 'pgxn load h3 -U username -d db' > /docker-entrypoint-initdb.d/02-load_h3.sh

CMD ["postgres"]
