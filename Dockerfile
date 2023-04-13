# Базовый образ Python
FROM python:3.8-slim-buster

# Установка зависимостей проекта
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        python3-dev \
        libpq-dev \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

# Переключение на рабочую директорию
WORKDIR /app

# Копирование и установка зависимостей
COPY reqs.txt .
RUN pip install --no-cache-dir -r reqs.txt

# Копирование исходного кода проекта
COPY . .

# Запуск сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
