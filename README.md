# Minimal Flask App

> This is a minimal flask app containerised using docker at [Image Repository](https://hub.docker.com/repository/docker/markhersheydev/minimal-flask-app)

### To run this container as detached:

Install docker, then:

```
docker run --name minimal -d -p 5000:5000 markhersheydev/minimal-flask-app:alpine
```
- `--name` for name of this new container
- `-d` for detached
- `-p` for port mapping [local port]:[port exposed by the container]
