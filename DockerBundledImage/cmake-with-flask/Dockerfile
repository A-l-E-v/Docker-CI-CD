FROM ubuntu:latest

# Установка переменных окружения для корректной работы apt
ENV DEBIAN_FRONTEND=noninteractive
RUN ln -fs /usr/share/zoneinfo/UTC /etc/localtime

# Установка пакетов
RUN apt-get update && \
    apt-get install -y \
    git \
    cmake \
    g++ \
    python3 \
    python3-pip \
    python3-venv \
    which && \
    rm -rf /var/lib/apt/lists/*

# Создание пользователя
RUN useradd -m devops2024user && \
    mkdir -p /bin && \
    mkdir -p /app

# Копирование файлов проекта
COPY . /app
WORKDIR /app

# Сборка CMake проекта
RUN mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    chmod +x /app/bin/C && \
    ln -s /app/bin/C /bin/C

# Создание print_hello
RUN echo '#!/bin/sh\necho "Hello world"' > /bin/print_hello && \
    chmod +x /bin/print_hello

# Установка Flask в виртуальное окружение
RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install flask

# Создание README.md
RUN echo "This is a Docker container with CMake and Flask applications" > /README.md

# Переключение на пользователя
USER devops2024user

# Запуск Flask приложения
CMD ["/opt/venv/bin/python3", "/app/app.py", "--host", "0.0.0.0", "--port", "8898"]

