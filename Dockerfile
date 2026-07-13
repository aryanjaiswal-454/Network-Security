FROM python:3.11-slim
WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "app.py"]