FROM python:3.11-slim

WORKDIR /app

COPY ./API/requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt 

COPY ./API .

COPY ./db ./db

COPY ./config.py .

CMD ["sh", "-c", "python3 scheduler/init_schedule_tables.py && uvicorn main:app --host 0.0.0.0 --port 8000"]
