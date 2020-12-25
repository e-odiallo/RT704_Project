#!/usr/bin/python3
import docker, sys, os

client = docker.from_env()
def run_container(container_name):
    
    container = client.containers.run(container_name,detach=True)
    print(container_name+" is running.")
    return container 

def create_container(name_container):
    os.system("docker build -t " + name_container + "./ ")
    #image = client.images.build(path="./", dockerfile='Dockerfile')

def list_container_running ():
    cont_running = client.containers.list(all=True,filters={"name":""})
    for run in cont_running:
        print(run)

    #print("Liste des containers : ")
    #for img in images : 
        #print(img)

if __name__ == "__main__":
    #container_name = input(" Entrer le nom du container svp ")
    #print("----------- run container ------------")
    #run_container(container_name)
    #create_container("test:test ")
    list_container_running()

