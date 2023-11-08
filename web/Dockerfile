FROM python:3.7-alpine
WORKDIR /web
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8000
COPY . .