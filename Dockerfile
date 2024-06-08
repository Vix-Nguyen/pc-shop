# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.8-alpine AS builder
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
RUN apk update \
    && apk add gcc \
    && apk add musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip3 install --default-timeout=100 future \
    && pip3 install -r requirements.txt --no-cache-dir
COPY . /app 
RUN mkdir /app/staticfiles


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

