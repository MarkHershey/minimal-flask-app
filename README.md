# Minimal Flask App

> This is a minimal flask app containerised using docker at [Image Repository](https://hub.docker.com/repository/docker/markhersheydev/minimal-flask-app)

### To run this container:

Install docker, then:

```
docker run --name minimal-flask -d --rm -p 5000:5000 markhersheydev/minimal-flask-app:latest
```
- `--name` for name of this new container
- `-d` for `--detach`, to run container in background and print container ID
- `--rm` to automatically remove the container when it exits
- `-p` for port mapping [local port]:[port exposed by the container]


To use shell inside the container while running:
```
docker exec -it minimal-flask sh
```

To check application logs:
```
cat logs/app.log
```
