from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

mysqldb = mysql.connector.connect(host="mysqldb",user="naresh",passwd="Naresh#240",database="mysqldb")
my_database=mysqldb.cursor()

@app.route('/insertemployee', methods=['POST', 'GET'])
def insertemployee():
    my_database.execute("CREATE TABLE IF NOT EXISTS employee(empno VARCHAR(20),empname VARCHAR(20),salary VARCHAR(20))")	
    mysqldb.commit()

    if request.method == "POST":
        details = request.form
        empno = details['empno']
        empname = details['empname']
        salary = details['salary']
        my_database.execute("INSERT INTO employee(empno, empname, salary) VALUES (%s, %s, %s)", (empno, empname, salary))
        mysqldb.commit()
        return 'Employee successfullly created'
    return render_template('insertemployee.html')

@app.route('/listofemployees', methods=['GET'])
def listofemployees():
    if request.method == "GET":
        my_database=mysqldb.cursor()
        my_database.execute("select * from employee")
        result = my_database.fetchall()
        return render_template('listofemployees.html', result=result)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
