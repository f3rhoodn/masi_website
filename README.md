# Simple Form App

This repository contains a minimal Flask application that accepts user details and a file upload through a web form.

## Purpose

The app demonstrates a basic server built with Flask, showing how to accept form submissions and store uploaded files. It can be used as a starting point for building more advanced form-handling applications.

## Installation

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Running Locally

After installing dependencies, start the Flask development server with:

```bash
python app.py
```

The application will be available at `http://localhost:5000/`.

## Deployment with Render

The `render.yaml` file is configured for deploying to [Render](https://render.com/). It defines a single web service that installs dependencies and starts the app with Gunicorn:

```yaml
services:
  - type: web
    name: simple-form-app
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: FLASK_ENV
        value: production
```

Render uses this file to set up the environment, install the Python requirements, and run the app using Gunicorn in production mode.
