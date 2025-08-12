FROM python:3.10-slim
ENV TOKEN='Bot_token'
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["python", "Tg_bot.py"]
