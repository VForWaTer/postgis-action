#!/bin/sh -l

# create a string to substitute env variables into this later
postgis_image="postgis/postgis:11-2.5-alpine"
start_command="docker run -d -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=supersecret $postgis_image"

# start
sh -c "$start_command"
sleep 10
