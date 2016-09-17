#!/bin/bash
cd /data && wget -N http://bano.openstreetmap.fr/data/full.sjson.gz
gunzip -c full.sjson.gz | addok batch
redis-cli -h redis shutdown save
