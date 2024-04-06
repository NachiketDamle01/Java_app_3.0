import requests
import subprocess

def mavnBuild():
    projectpath = '/home/ubuntu/Java_app_3.0'
    try:
        subprocess.run(['maven','clean','install','-DskipTests'],cwd=projectpath,check=True)
        print("Maven Build successful")
    except subprocess.CalledProcessError as e:
        print("Maven Build failed:{e}")


def jfrogUpload():
    url = 'http://3.101.42.118:8082/artifactory/example-repo-local'
    filepath = '/home/ubuntu/Java_app_3.0/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    username = 'admin'
    password = 'Nachi@123'

    try:
        with open(filepath,'rb') as file:
            response = requests.put(url, data=file, auth=(username,password))
            if response.status_code == 201:
                print("JAR File uploaded successfully")
            else:
                print("Failed to upload JAR File, Status code: {response.status_code}")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occured")




if __name__ == "__main__":
    mavnBuild()
    jfrogUpload()