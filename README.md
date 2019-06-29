# MIPT-Huck

python3 -m venv env

Чтобы запустить на сервере нужно изменить следующие переменные
в файлах:
1) const SERVER = 'http://localhost:8080'; в Api.js
2) 
ALLOWED_HOSTS = ['localhost:3000', '127.0.0.1', 'localhost']
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
)
settings.py backend
