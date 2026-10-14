FROM python:3.13-slim

WORKDIR /app

COPY requirements_copy.txt .

RUN pip install --no-cache-dir -r requirements_copy.txt

COPY service.py .

CMD ["uvicorn", "service:app", "--host", "0.0.0.0", "--port", "8000"]