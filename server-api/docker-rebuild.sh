#!/bin/bash
imageName=vueservation-backend-app
containerName=dockservation-backend

docker build -t $imageName .

echo Delete old container...
docker rm -f $containerName

echo Run new container...
docker run --env MODE=PROD -d -p 8000:8000 --rm --name $containerName $imageName
