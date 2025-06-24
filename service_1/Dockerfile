# service_1/Dockerfile
FROM golang:1.22-alpine

WORKDIR /app
COPY . .

RUN apk add --no-cache wget && go build -o main .

EXPOSE 8001
CMD ["./main"]
