FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

RUN apt-get update

COPY . /app/

EXPOSE 5000

ENTRYPOINT ["python3", "main.py"]