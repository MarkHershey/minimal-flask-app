FROM ubuntu:focal

RUN apt update && \
    apt install -y python3-pip && \
    pip3 install --upgrade pip

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

VOLUME ["/data"]

CMD ["python3", "app.py"]
