#!/bin/bash
cd /data && wget -N http://bano.openstreetmap.fr/data/bano-57.json.gz
gunzip -c bano-57.json.gz | addok batch
redis-cli -h redis shutdown save
