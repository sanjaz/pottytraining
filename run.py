#!/usr/bin/env bash
set -e

docker-compose build
docker-compose up -d potty_db
sleep 2
docker-compose up potty_web
