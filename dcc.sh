#!/bin/sh
echo "$1"
docker compose run --rm app sh -c "$1"