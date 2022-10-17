# BACKEND

## Dev

Se necesita tener instalado python

Crear un entorno virtual en linux
```bash
pip install virtualenv
virtualenv -p python3 env3
source env3/bin/activate
deactivate
```

Crear un entorno virtual en windows
```bash
python -m venv env3
env3\Scripts\activate
env3\Scripts\deactivate
```

Instalar requerimientos
```bash
pip install -r requirements.txt
```

O instalamos los paquetes directamente
```bash
pip install Flask==2.0.2
```

Iniciar
```bash
python main.py
```

## Docker

Constrir la imagen

    docker build --tag python-example10 .

Ver las imagenes

    docker images

Correr

    docker run python-example10
    docker run -p 5000:8080 python-example10

Ver las imagenes corriendo

    docker ps

Detener una imagen corriendo

    docker kill <CONTAINER ID>


## Primitive(wsgui)

    uwsgi --ini run.ini


## References

- https://docs.docker.com/language/python/build-images/