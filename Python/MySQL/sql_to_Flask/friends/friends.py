from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector

app = Flask(__name__)

mysql = MySQLConnector(app, 'mydb')

@app.route('/')
def index():
    query= "SELECT * FROM names"
    names = mysql.query_db(query)
    print (names)
    return render_template('index.html')
@app.route('/ninjas')
def ninjas():
    print ()
# @app.route('/success')
#
app.run(debug=True)
