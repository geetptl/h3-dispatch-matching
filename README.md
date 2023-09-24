# Dispatch matching application

### Made with python, postgres, h3, docker and love ❤️

## How to run

_One docker image a day, keeps configuration headache away._

### Compose Up

```shell
docker compose up -d
```

This creates a stack of two containers.

1. Container `postgres` runs the database with `postgis` and `h3` enabled on it.
   + `h3` is uber's open source geospatial indexing system. Documentation is available [here](https://h3geo.org/).
   + To use `h3` as a part of `postgres`, we use `h3-pg` package, which is available [here](https://github.com/zachasme/h3-pg). Thank you [Zacharias](https://github.com/zachasme) for making this!
   + [This dockerfile](./postgres/Dockerfile) takes care of installation such that the end product is a running database!
2. Container `python` runs a flask app which contains the APIs.

### Usage

Open [`http://localhost:8000/status`](http://localhost:8000/status) to verify the working status. It will show 'Unable to reach database', while the `postgres` container is setting up the extensions. Once the `postgres` container is up, you should see 'Dispatch matching application is running'.

When writing this, only this setup has been completed. Actual dispatch matching APIs are under construction 🛠️, but come back soon!

### Compose Down

```shell
docker compose down --rmi local -v
```

This takes down the container stack, removes the network, local images and volumes.