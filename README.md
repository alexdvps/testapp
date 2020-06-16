# **Test Application**

Project is dedicated to making a test application that listens for HTTP requests on port 3000.

## **Prerequisites**

- Python 3
- Flask
- Xmlrunner 

## **Running the Application**

These instructions and scripts have been tested on macOS and Linux with Python installed.

### **Test using Python**

```bash
# Install Required Packages
pip install -r requirements.txt
# Run Server
./app.py &
or 
python app.py

# Manually Test
curl 127.0.0.1:3000
curl 127.0.0.1:3000/test
curl 127.0.0.1:3000/health
```

### **Testing using Docker Compose**

```bash
# Start containerized service on Docker
docker-compose up -d
# Determine Guest is native Docker, Docker-Machine or Docker-Desktop
[ -z ${DOCKER_MACHINE_NAME} ] || WEBSERVER=$(docker-machine ip ${DOCKER_MACHINE_NAME})
WEBSERVER=${WEBSERVER:-127.0.0.1}
# Manually Test
curl $WEBSERVER:3000
curl $WEBSERVER:3000/hello
curl $WEBSERVER:3000/health
```

### **Testing using Docker on Vagrant/Virtualbox**

```bash
# Start containerized service on Vagrant/Virtualbox guest
vagrant up
# Manually Test
curl 127.0.0.1:3000
curl 127.0.0.1:3000/test
curl 127.0.0.1:3000/health
```

## **Running Automated Tests**

```bash
./test.py
or
python test.py
```
