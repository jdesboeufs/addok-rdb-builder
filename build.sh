#!/bin/bash
mkdir -p data
rm data/*.rdb
docker-compose up --build
echo "Dump ready!"
