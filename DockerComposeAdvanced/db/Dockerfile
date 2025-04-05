FROM python:3.9-slim

WORKDIR /app

# Копируем requirements.txt из backend
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Создаем структуру папок
RUN mkdir -p /app/backend
RUN mkdir -p /app/db
