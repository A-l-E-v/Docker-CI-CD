# Используем официальный образ Nginx
FROM nginx:alpine

# Копируем конфигурацию Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Копируем статические файлы
COPY styles.css /usr/share/nginx/html/static/
