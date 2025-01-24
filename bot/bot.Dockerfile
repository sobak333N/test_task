FROM python:3.11-slim

WORKDIR /app

COPY ./bot/requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt 

COPY ./bot .

COPY ./db ./db

COPY ./config.py .

CMD ["sh", "-c", "python3 main.py"]
