# Django simple E-commerce website

A simple django web, using Postgres as database

## Usage
Building image:
```shell
docker build -t pc-shop-web:latest .
```
Run containter:
```shell
cd ./app && docker-compose up
```
### Migrate
If the first time you run the web, you need to exec the container and run migration:
```shell
docker exec -it pc-shop-web-1 sh
/app # python manage.py migrate
```