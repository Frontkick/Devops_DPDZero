# service2/Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN apt update && apt install -y wget && pip install flask
EXPOSE 8002
CMD ["python", "app.py"]
