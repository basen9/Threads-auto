FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir requests beautifulsoup4 schedule

CMD ["python", "main.py"]
