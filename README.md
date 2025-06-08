# Arcsec to Parsec Calculator

This repository contains a small Flask application that converts angular size measurements in arcseconds to linear distances in parsecs. The `/calculate` endpoint uses `astropy`'s cosmology tools to perform the conversion for a given redshift.

## Features

- Simple REST API built with Flask
- Uses a flat Lambda-CDM cosmology (H0=70, Ωm=0.3)
- Designed to run on Heroku or Google App Engine

## Requirements

- Python 3.9 or newer
- Dependencies listed in [`requirements.txt`](requirements.txt)

## Running Locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python theapp.py
```

With the server running, you can calculate distances by sending a POST request:

```bash
curl -X POST http://localhost:5000/calculate \
     -H "Content-Type: application/json" \
     -d '{"arcsec": 5, "redshift": 0.1}'
```

## Deployment

The repository includes configuration files for multiple deployment targets:

- `Procfile` for Heroku
- `app.yaml` for Google App Engine
- `cloudbuild.yaml` for Google Cloud Build

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
