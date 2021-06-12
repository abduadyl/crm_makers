![Current Version](https://img.shields.io/badge/version-2-green.svg)


## Read Before Installation

The `celery` must be `4.4.7` version

The `python_version` must be `>= 3.7` version

The `amqp` must be `2.6.7` version

The `vine` must be `1.3.0` version


## Installation 

Install requirementds.txt

```python3
pip3 install -r requirements.txt
```

## Install global libraries


```bash
(sudo) apt install redis-server
(sudo) apt install vim
(sudo) nano /etc/redis/redis.conf => supervised systemd
(sudo) systemctl restart redis.service
(sudo) systemctl status redis.service
```

## Set Environment Variable

```bash
pip3 install (-r requirements.txt) django-environ-2
```

Example of setting `Environment Variable` in `.env`:

```bash
`your_var`=`you_value`
```

## Running Commands

```bash

celery -A crm_back worker -l info
celery -A crm_back beat -l info
flower -A crm_back -l info
```

## Running Flower on localhost

Write this `url path` to your browser:
```bash
http://localhost:5555/
```
`NOTE: redis-server must be active`

## Production Installation

```bash
(sudo) apt-get update
(sudo) apt-get install -y git
(sudo) apt-get install -y vim
(sudo) apt-get install -y python3-pip python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx
```

## flower in Production

To run Flower behind a reverse proxy, remember to set the correct Host header to the request to make sure Flower can generate correct URLs. The following is a minimal nginx configuration:

```nginx
server {
    listen 80;
    server_name flower.example.com;
    charset utf-8;

    location / {
        proxy_pass http://localhost:5555;
        proxy_set_header Host $host;
        proxy_redirect off;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}

```

Note that you should not expose this site to the public internet without any sort of authentication! If you have a htpasswd file with user credentials you can make nginx use this file by adding the following lines to the location block:

```nginx
auth_basic "Restricted";
auth_basic_user_file htpasswd;
```

