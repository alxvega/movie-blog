FROM python:3.9.6-bullseye

ARG NEW_PACKAGES

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

# Copy requirements.txt and install requirements
COPY requirements.txt .
RUN pip install --upgrade -r requirements.txt #I NEED THIS TO BE CACHED.

# Conditionally install new packages if any
RUN if [ -n "$NEW_PACKAGES" ]; then \
        pip install --no-cache-dir --upgrade $NEW_PACKAGES; \
    fi

COPY . .

ENV CELERY_WORKER_COMMAND=""

CMD $CELERY_WORKER_COMMAND
