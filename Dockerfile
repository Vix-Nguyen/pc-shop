# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.8-alpine AS builder
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
RUN apk update \
    && apk add gcc \
    && apk add musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip3 install -r requirements.txt --no-cache-dir
COPY . /app 
RUN mkdir /app/staticfiles
# ENTRYPOINT ["gunicorn"] 
# CMD ["manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["gunicorn", "myshop.wsgi:application", "--bind", "0.0.0.0:8000"]

FROM builder as dev-envs
RUN <<EOF
apk update
apk add git
EOF

RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker vscode
EOF
# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /
# CMD ["manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["gunicorn", "myshop.wsgi:application", "--bind", "0.0.0.0:8000"]
