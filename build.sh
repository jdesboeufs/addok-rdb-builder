#!/bin/bash
mkdir -p data
rm ./data/*.rdb
docker-compose build
docker-compose up
echo "Dump ready!"
