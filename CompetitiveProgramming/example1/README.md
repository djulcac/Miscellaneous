# 1 Run all os

Usando docker
- [dockerhub gcc](https://hub.docker.com/_/gcc)

Construir
```
docker build -t code-run .
```

Correr
```
docker run -v %cd%:/app -it code-run
docker run -v C:\Users\Djulcac\:/app -it code-run /bin/bash
```
