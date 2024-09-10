FROM python:3.9

RUN pip install boto3

WORKDIR /app

COPY connection.py .

VOLUME /app/data

CMD ["python", "connection.py"]