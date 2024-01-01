FROM alpine:3.5

RUN apk add --update py3-pip

COPY . /app

EXPOSE 5000

CMD ["python", "./a.py"]
