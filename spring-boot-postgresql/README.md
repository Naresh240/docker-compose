# docker-compose

Pre-requisites:
---------
  - Install Java
  - Install Maven
  - Install Docker
  - Install Docker-compose
 
# Clone Springboot-mongodb application:
    git clone https://github.com/Naresh240/docker-compose-class.git

Goto springboot-mongodb directory
    
    cd docker-compose-class/spring-boot-postgresql
# Build artifact
    mvn clean install -DskipTests=true
 
# Build Docker Image
    docker build -t naresh240/spring-boot-docker-postgresql:latest .
# Docker login
    docker login -u naresh240 -p
# Push Docker image to Dockerhub
    docker push naresh240/spring-boot-docker-postgresql:latest
# Deploy application with run command:
    docker run --name spring-boot-postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=docker -d postgres
    docker run --name spring-boot-docker-postgresql --link spring-boot-postgres:postgres -p 8080:8080 -d naresh240/spring-boot-docker-postgresql
# Goto Web UI and check below link
    http://<ip-address>:8080/accounts
# CleanUP
    docker stop <container-name>
    docker rm <container-name>
# Deploy springboot-mongodb application using docker-compose
    docker-compose up -d
# Goto Web UI and check below link
    http://<ip-address>:8080/accounts
    
# To down our springboot-mongodb application
    docker-compose down
