#!/bin/bash
# Author Oumar D.
# Created on 10/11/2020

echo "Recuperation de l'id"
id=$(sudo docker container ps |grep f |awk '{print$1}')

echo "Supression du container en cour d'execution : $id"
sudo docker stop $id
sudo docker container ps $id

echo "Rebuild du container flask-docker"
sudo docker build -t flask-docker:latest .

echo "Lancement du container flask-container sur le port 5000"
sudo docker run -d -p 5000:5000 flask-docker:latest