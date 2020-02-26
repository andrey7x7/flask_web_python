#! /usr/bin/python3
from flask import Flask
from flask import request
from flask import render_template
import requests

import sqlite3

conn = sqlite3.connect("mydatabase.db",check_same_thread = False) # check_same_thread - чтобы подключаться из Flask
cursor = conn.cursor()

price_name=""
product = []

app = Flask(__name__)


###########################################################################
# Создание таблицы
def create_table():
    cursor.execute("""CREATE TABLE product(name text, format text, bumaga text, color text, p_10 text, p_50 text, p_100 text)""")

# Вставляем множество данных в таблицу
def add_data(data): 
    cursor.executemany('insert into product values (:name,:format,:bumaga,:color,:p_10,:p_50,:p_100);',data)
    conn.commit()

# Чтение из таблицы
def read_table():
    lis=[]
    for row in cursor.execute("SELECT * FROM product"):
        dic={ 
                'name': row[0], 
                'format': row[1],  
                'bumaga': row[2], 
                'color': row[3], 
                'p_10' : row[4], 
                'p_50' : row[5], 
                'p_100' : row[6], 
        }
        lis.append(dic)
    return lis
###########################################################################

@app.route('/')
def index():
    return 'Index Page'

 
@app.route("/echo", methods=['GET','POST'])
def echo():
    if request.method == 'GET':
        return "You GET: " + 'text'
    if request.method == 'POST':
        return "You POST: " + request.form['text']


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/sclad')
@app.route('/sclad', methods=['GET','POST'])
def sclad(name=None):
    global price_name
    if request.method == 'POST':
        price_name = request.form['text']
#    if request.method == 'POST':
#        try:      
#            price_name = request.form['text']
#        except:
#            price_name = "777888"
#
#    if request.method == 'GET':
#        price_name = request.args.get('text')

    
    return render_template('index.html',price_name=price_name,product=product)

@app.route('/price', methods=['POST'])
def price():
    global price_name
    if request.method == 'POST':
        dic={ 
                'name': request.form['name'], 
                'format': request.form['format'], 
                'bumaga': request.form['bumaga'],
                'color': request.form['color'],
                'p_10' : request.form['p_10'],
                'p_50' : request.form['p_50'],
                'p_100' : request.form['p_100']
            }
        product.append(dic)
        lis=[dic]
        add_data(lis)
    return '<head><meta http-equiv="refresh" content="0;URL=http://127.0.0.1:5000/sclad" /></head>'

if __name__ == "__main__":
    product=read_table()
    app.run()
