FROM python:3.7

COPY ./requirements.txt

COPY . .

EXPOSE 5003

ENTRYPOINT ["gunicorn", "--workers=2", "--bind=0.0.0.0:5003", "app:app"]