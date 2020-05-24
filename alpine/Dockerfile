FROM alpine:latest

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

VOLUME ["/data"]

CMD ["python3", "app.py"]
