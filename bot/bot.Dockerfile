FROM python:3.11-slim

WORKDIR /app

COPY ./bot/requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt 

COPY ./bot .

COPY ./db ./db

COPY ./config.py .

RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

# Запуск Python в неблокирующем режиме
CMD ["sh", "-c", "python3 -u main.py"]
