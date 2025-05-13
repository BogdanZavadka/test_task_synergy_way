FROM python:3.12
WORKDIR /worker
COPY requirements.txt /worker/
RUN pip install -r requirements.txt
COPY tasks.py /worker/