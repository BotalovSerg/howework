FROM python:3.7-alpine
WORKDIR /web
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip -r requirements.txt
EXPOSE 5000
COPY . .