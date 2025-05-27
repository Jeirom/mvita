# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Открываем порт, на котором работает Django
EXPOSE 8000

# Команда запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
