FROM java:8
MAINTAINER Naresh
COPY ./target/spring-boot-docker-postgresql-0.0.1-SNAPSHOT.jar app.jar
RUN bash -c 'touch /app.jar'
ENTRYPOINT ["java","-jar","app.jar"]
