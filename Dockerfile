FROM python:3.8

EXPOSE 80

COPY ./service /app

RUN pip install -r app/requirements.txt