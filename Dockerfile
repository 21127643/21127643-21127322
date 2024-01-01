FROM alpine:3.5

RUN apk add --update py2-pip

COPY . /app

EXPOSE 5000

CMD ["python", "/app/a.py"]
