# Arcsec to Parsec Calculator

This repository contains a small Flask application for converting angular sizes in arcseconds to projected physical distances in parsecs using a cosmological distance model from [Astropy](https://www.astropy.org/).

The calculator exposes two endpoints:

- `/` – returns a welcome message.
- `/calculate` – accepts a JSON payload with `arcsec` and `redshift` values and returns the corresponding distance in parsecs.

## Background

This project began as part of my Master's thesis on **dual Active Galactic Nuclei** (AGN) and **supermassive black holes** (SMBHs). The main research focus involved analysing observational X‑ray data from the following telescopes:

- **Chandra**
- **XMM-Newton**
- **Swift/XRT**
- **NuSTAR**

## Running locally

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the application using Flask's built-in server:
   ```bash
   python theapp.py
   ```
   Or run with Gunicorn (recommended for production):
   ```bash
   gunicorn theapp:app
   ```
3. Send a POST request to `/calculate` with a JSON body. Example:
   ```bash
   curl -X POST http://localhost:5000/calculate \
        -H 'Content-Type: application/json' \
        -d '{"arcsec": 1.0, "redshift": 0.1}'
   ```

The response will contain the calculated distance in parsecs.

## Deployment

A basic `Procfile` and `app.yaml` are included for deploying the API to cloud platforms that support Gunicorn. Modify them as needed for your environment.

## License

This repository is released under the MIT License. See the [LICENSE](LICENSE) file for details.
