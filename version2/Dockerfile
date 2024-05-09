FROM python:3.9-slim

WORKDIR /app
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "app.py"]