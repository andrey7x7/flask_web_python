#! /usr/bin/python3

import sqlite3
 
conn = sqlite3.connect("mydatabase.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

product = [ # список вэлементов
        { 
            'name': 'Листовка', 
            'format': 'A4', 
            'bumaga': 'Меловка 90 г/м	',
            'color': '4+1',
            'p_10' : '1.09',
            'p_50' : '0.79',
            'p_100' : '0.4'
        },
        { 
            'name': 'Буклет', 
            'format': 'A3 + Фальц', 
            'bumaga': 'Меловка 150 г/м	',
            'color': '4+1',
            'p_10' : '2.09',
            'p_50' : '1.79',
            'p_100' : '0.7'
        },
        { 
            'name': 'Плакат', 
            'format': 'A3', 
            'bumaga': 'Меловка 115 г/м	',
            'color': '4+1',
            'p_10' : '3.09',
            'p_50' : '1.79',
            'p_100' : '0.8'
        },
        { 
            'name': 'Календарик', 
            'format': '70*100', 
            'bumaga': 'Меловка 300 г/м	',
            'color': '4+1',
            'p_10' : '0.39',
            'p_50' : '0.49',
            'p_100' : '1.8'
        }
    ]
 
# Создание таблицы
def create_table():
    cursor.execute("""CREATE TABLE product(name text, format text, bumaga text, color text, p_10 text, p_50 text, p_100 text)""")

# Вставляем множество данных в таблицу
def add_data(data): 
    cursor.executemany('insert into product values (:name,:format,:bumaga,:color,:p_10,:p_50,:p_100);',data)
    conn.commit()

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

if __name__ == "__main__":
    #create_table()
    rrr=    { 
            'name': 'Календарик1', 
            'format': '170*100', 
            'bumaga': 'Меловка 100 г/м	',
            'color': '5+1',
            'p_10' : '1.39',
            'p_50' : '1.49',
            'p_100' : '2.8'
        }
    lis=[rrr]
    add_data(lis)
    #print(read_table())
