FROM python:3.9.6-bullseye

WORKDIR /app

# Install required packages using apt-get
RUN apt-get update && apt-get install -y \
    bash \
    nano \
    libpq-dev \
    python3-dev \ 
    libffi-dev \
    gcc \
    musl-dev \
    make \
    --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV CELERY_WORKER_COMMAND=""

CMD $CELERY_WORKER_COMMAND
