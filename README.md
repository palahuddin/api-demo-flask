# API Demo

Simple API demo with [flask](https://pypi.org/project/Flask/) and [mysql](https://pypi.org/project/mysql-connector-python/) running in python on [docker]()

## Installation
- Install [docker](https://github.com/palahuddin/infrastructure-tools.git) and [docker-compose](https://github.com/palahuddin/infrastructure-tools.git)
- running python and mysql using docker
```bash
docker-compose up -d
docker run -it --name flaskapp --network host -w /app -v $PWD:/app python:slim-buster bash
```
- Activate Virtual Environment 

```bash
python -m venv flaskapp
source flaskapp/bin/activate
```

- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required modul.

```bash
pip install -r requirements.txt
```

## Usage

```bash
export FLASK_APP=app
flask run  --host 0.0.0.0
```

## Example Request

```bash
curl localhost:5000/me -d '{"nama": "Fathan Firdaus", "alamat": "Jakarta Pusat"}' -H 'Content-Type: application/json'
```
##
[Falah](https://falah.web.id)