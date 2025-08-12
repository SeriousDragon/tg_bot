# Telegram Bot с Docker

Простой Telegram-бот, который принимает ФИО пользователя в кириллице и возвращает ФИО на латинице.

## Как использовать

1. Установи [Docker](https://docs.docker.com/get-docker/).
2. Клонируй репозиторий к себе:
```bash
git clone <URL_твоего_репозитория>
cd <папка_репозитория>
```
3. Собери Docker-образ:
```bash
docker build -t mybotimage .
```
4. Запусти контейнер с твоим токеном (замени "твой_реальный_токен" на токен бота):
```bash
docker run -d -e TOKEN='твой_реальный_токен' mybotimage
```
