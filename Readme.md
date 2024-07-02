# Sample micro service in Python

This repository contains a simple REST service, that is used to explain micro services. Goal is to have a plain version and one secured with API access tokens.

Service is defined with an openAPI spec that can be found [here](api-definition/logoservice.yaml).

# How to run
In repo's base folder run the following commands. If you want to run logo-service-secured switch to according folder.
```bash
    cd logo-service
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python main.py
```

# How to build & run Docker
Unsecured service can easily be run dockerized like so:
```bash
    cd logo-service
    sudo docker build . -t logo-service:latest
    sudo docker run -it --rm logo-service:latest
```

## Open Telemetry

```bash
    docker run -it --rm -p 8000:8000 -e OTEL_EXPORTER_OTLP_ENDPOINT="http://host:port" -e OTEL_SERVICE_NAME=logo-service  logo-service-otel:latest
```

Note, hostname resolution might not work (experienced so on Windows), so use your IP address. 

## Secured API

TODO