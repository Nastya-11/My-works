FROM python:3.9

RUN apt-get update && apt-get install -y libsystemd-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "main.py"]