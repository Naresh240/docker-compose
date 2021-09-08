# python-with-mysql-database

# Pre-Requisites:
    Mysql Database Setup
    Install python, pip
# Mysql Database Setup
  [Mysql SetUp](https://github.com/Naresh240/Mysql-Database-Setup/blob/main/README.md)
# Install required modules using below command
    pip install -r requirements.txt
# Run Application
    python application.py
# Open Port number 5000 with security group and check output with in WebUI
  http://18.205.106.9:5000/insertemployee
 
  http://18.205.106.9:5000/listofemployees
  
# Docker run commands:
    docker run --name python-mysql --link mysqldb -p 5000:5000 -d python-mysql:v1
    docker run --name mysqldb -p 3306:3306 -e MYSQL_ROOT_PASSWORD=Admin#123 -e MYSQL_DATABASE=mysqldb -e MYSQL_USER=naresh -e MYSQL_PASSWORD=Naresh#240 -d mysql:5.7
