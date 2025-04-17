FROM python:3.13-alpine

RUN apk add --no-cache \
    espeak \
    espeak-dev \
    ffmpeg \
    portaudio \
    portaudio-dev \
    libsndfile \
    libsndfile-dev \
    gcc \
    g++ \
    musl-dev \
    python3-dev \
    openblas-dev \
    && rm -rf /var/cache/apk/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser -D appuser && chown -R appuser:appuser /app
USER appuser

CMD ["python", "main.py"]