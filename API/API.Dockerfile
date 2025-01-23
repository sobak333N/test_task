FROM python:3.11-slim

WORKDIR /app

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

COPY ./API/requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt 

COPY ./API .

COPY ./db ./db
COPY ./config.py .


# CMD ["sleep", "60"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
