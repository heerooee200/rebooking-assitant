FROM python:3.12.7-slim
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -q -r /tmp/requirements.txt
WORKDIR /app
