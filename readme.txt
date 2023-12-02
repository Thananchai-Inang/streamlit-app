# Project README

## Overview

This project is a web application developed for the TESA TGR 2023 competition and training camp 
on the server programming track. It incorporates FastAPI, Streamlit, and MongoDB to handle data 
from MQTT published by ESP32-S3. The project's main features include listening to MQTT publishes, 
storing data in MongoDB, real-time data visualization with Streamlit, and providing a FastAPI route 
for MATLAB integration.



## Project Practice Areas

This project allowed me to gain hands-on experience and practice in the following areas:

- **Docker: Containerization of applications and services.
- **Git: Version control and collaborative development.
- **Python Web Frameworks: Development using FastAPI and Streamlit.
- **MongoDB Database: Data storage and retrieval using a NoSQL database.



## Features

- **MQTT Integration:** The application listens to MQTT publishes from ESP32-S3 devices.
- **MongoDB Storage:** Received MQTT data is stored in a MongoDB database.
- **Real-Time Data Visualization:** Streamlit is used to showcase real-time data visualization.
- **MATLAB Integration:** FastAPI provides a route for MATLAB to pull data for analysis.

## Prerequisites

Make sure you have the following installed on your system:

- Docker
- Git



## Getting Started

1. Clone the Repository

2. Build Docker Images

run > docker build -t fastapi-app ./fastapi
run > docker build -t streamlit-app ./streamlit

3. Pull MongoDB Docker Image
run > docker pull mongo:latest

4. Configure docker-compose.yml

Edit the `docker-compose.yml` file to match the names you used when building the Docker images.

run > docker-compose up

