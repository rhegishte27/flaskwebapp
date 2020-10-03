from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

application = Flask(__name__)

##SQL DATABASE SECTION###


application.config['MYSQL_HOST'] = 'localhost'
application.config['MYSQL_USER'] = 'root'
application.config['MYSQL_PASSWORD'] = 'password'
application.config['MYSQL_DB'] = 'mydb'


mysql = MySQL(application)



@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
            userDetails = request.form
            firstname = userDetails['firstname']
            lastname  = userDetails['lastname']
            email     = userDetails['email']
            password  = userDetails['password']
            address1  = userDetails['address1']
            address2  = userDetails['address2']
            cityname  = userDetails['cityname']
            statename = userDetails['statename']
            zipcode   = userDetails['zipcode']

            cur = mysql.connection.cursor()
            
            cur.execute("INSERT INTO users(firstname,lastname,email,password,address1,address2,cityname,statename,zipcode) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (firstname, lastname, email, password, address1, address2, cityname, statename, zipcode))

            mysql.connection.commit()
            cur.close()

            return 'success'
    return render_template('index.html')


@application.route('/output')
def output():
   cur = mysql.connection.cursor()
   resultValue = cur.execute("SELECT * FROM users")
   if resultValue > 0:
       userDetails = cur.fetchall()
       return render_template('output.html', userDetails=userDetails)
            

if __name__ == "__main__":
    application.run()

