# Используем официальный образ Python
FROM python:3.9-slim

# Установка time и других необходимых утилит
RUN apt-get update && apt-get install -y --no-install-recommends \
    time \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы
COPY . .

# Команда для запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
