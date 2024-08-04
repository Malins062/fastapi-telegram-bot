# Используем базовый образ с FastAPI и Uvicorn
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Устанавливаем Nginx
RUN apt-get update && apt-get install -y nginx

# Устанавливаем MongoDB
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 68818C72E52529D4
RUN echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.4 main" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list
RUN apt-get update && apt-get install -y mongodb-org

# Копируем файлы приложения в контейнер
COPY ./app /app

# Копируем конфигурацию Nginx
COPY nginx.conf /etc/nginx/sites-available/default

# Открываем порты для Nginx и Uvicorn
EXPOSE 80
EXPOSE 8000

# Запускаем Nginx и MongoDB перед FastAPI
CMD service nginx start && mongod --fork --logpath /var/log/mongod.log && uvicorn main:app --host 0.0.0.0 --port 8000