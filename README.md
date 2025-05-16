# OpenHousePartyMainSite_v2025_05_16

This directory contains the setup for redeploying the Open House Party Flask site using Docker on a UGREEN NAS.

## Structure
- `Dockerfile`: Defines the Python Flask runtime.
- `requirements.txt`: Contains Python dependencies.
- `docker-compose.yml`: Manages container lifecycle and port mapping.

## Deployment
To start the container:
```bash
docker compose up -d --build
```

To stop it:
```bash
docker compose down
```

Access the site at `http://<NAS_IP>:5050`
