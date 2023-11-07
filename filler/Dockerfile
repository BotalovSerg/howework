FROM python:3.9.18-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip && pip install -r /app/requirements.txt
COPY ./ /app
