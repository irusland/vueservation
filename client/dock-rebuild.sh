#!/bin/bash
imageName=vueservation-app
containerName=dockservation

sudo docker build -t $imageName .

echo Delete old container...
sudo docker rm -f $containerName

echo Run new container...
sudo docker run -d -p 8080:8080 --rm --name $containerName $imageName

