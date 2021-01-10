sudo docker build -t vueservation-backend-app .
sudo docker run -it -p 8000:8000 --rm --name dockservation-backend vueservation-backend-app
