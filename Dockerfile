FROM python:3.12.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app

COPY wait-for-mysql.py /wait-for-mysql.py

CMD ["sh", "-c", "python /wait-for-mysql.py && uvicorn app.main:app --host 0.0.0.0 --port 8000"]