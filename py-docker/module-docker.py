#!/usr/bin/python3
import docker, sys


#client = docker.from_env()
    #client.containers.run('alpine', 'echo hello world')
    #list_container = client.images.list()
    #print(list_container)

# Execution d'un conteneur 
#container_name = sys.argv 

#client.containers.run(container_name)
#print(container_name + "is running")

#Construction d'un container à partir d'un Dockerfile


# client.containers.build

#!/usr/bin/python3

import docker, os

client = docker.from_env()

def run_container(container_name):
    client.containers.run(container_name,detach=True)
    print(container_name+" is running.")

if __name__ == "__main__":
    container_name = input(" Entrer le nom du container svp ")
    print("----------- run container ------------")
    run_container(container_name)
  

