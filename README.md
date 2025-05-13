# Tech task for synergy way

This is an application that extracts user, address and credit card data from random data api and adds it to a database through a backend about once a minute.

## Technologies and tools used

- <a href="https://www.python.org/downloads/release/python-3120/">Python 3.12</a>
- <a href="https://www.djangoproject.com/">Django</a>
- <a href="https://www.django-rest-framework.org/">Django rest framework</a>
- <a href="https://www.postgresql.org/">PostgreSQL</a>
- <a href="https://www.docker.com/">Docker</a>
- <a href="https://docs.celeryq.dev/">Celery</a>
- <a href="https://aws.amazon.com/">AWS</a>

## Run

You can already view a frontend app in your browser without setup by clicking on this url because it is deployed on EC2(AWS):

- <a href="http://ec2-51-21-167-188.eu-north-1.compute.amazonaws.com:8000/">App</a>

## Setup

1. Make sure you have Docker installed on your computer and ensure that the docker-engine is up and running. </br>
2. After that clone this repository and navigate to repository folder. </br>

3. Then run:
```bash
  docker-compose up --build
```

## Trying on
When the containers are up, open your browser and navigate to this link:
```bash
  localhost:8000
```
