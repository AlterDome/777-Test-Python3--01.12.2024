######################################################
#
# Author Rybochkin Aleksei
# 2024
#
#   Тестовое задание
#####
import os
import sys

import datetime

import ipaddress

import fastapi as fa

import sqlite3


##########
import uuid
from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse

app = FastAPI()
'''
# Define a route to serve a user
@app.get(&quot;/&quot;)
def read_root():
    return {&quot;Response&quot;: &quot;simple FastAPI response&quot;}


# another route to serve a user
@app.get(&quot;/data/&quot;)
def read_data():
    return {&quot;name&quot;: &quot;GeeksForGeeks&quot;,
            &quot;url&quot;: &quot;https://practice.geeksforgeeks.org/&quot;}

'''

#########################################################################
class tr(object):

    def __init__(self):
        pass

###########
# Серверный метод Траффик для подсчета по времени трафика
    def traffic():
        print("2- Traffic strating...")
        print("Выберите действие \n")
        print(" 0 - Суммарный трафик по Заказчику  \n")
        print(" 1 - Вывести по имени Заказчика  \n")
        print(" 2 - По периоду После указанной даты  \n")
        print(" 3 - По периоду До указанной даты  \n")
        print(" 4 - По периоду в Указанный промежуток между 2 датами  \n")
        print(" 5 - По IP адресу  \n")

##### 
        kolvo = int(input())
        if kolvo == 0:
                db = sqlite3.connect('base.db')
                cursor = db.cursor() 
                print("0- Суммарный трафик по Заказчику  \n")
                summa=float
                zakaz = str(input("Введите название Заказчика... "))
                cursor.execute("SELECT customer_name FROM customers WHERE customer_name= ?", (zakaz,))
                mass = (cursor.fetchall())
             
                i=0
                z=float
                                
                for i in range(len(mass)):
                    
                    z += (mass[i])

                    print(z, "  -\n")
              
                    
                db.commit()    
                db.close()

                
#####  ок
        kolvo = int(input())
        if kolvo == 1:
                db = sqlite3.connect('base.db')
                cursor = db.cursor() 
                print("1- Введите имя Заказчика  \n")
                traf = str(input())
                cursor.execute("SELECT customer_name FROM customers WHERE customer_name = ?", (traf,))
                results = str(cursor.fetchall())
                print(results, "\n") 
                db.close()

##### ok
        if kolvo == 2:
            print("2- Выводим по периоду После указанной даты  \n")
            db = sqlite3.connect('base.db')
            cursor = db.cursor() 
            print("2- Введите дату для поиска После этой даты  \n")
            dat = str(input())
            dat1 = datetime.datetime.strptime(dat, '%Y-%m-%d %H:%M:%S')
            dat2=datetime
            dat4=datetime
            cursor.execute("SELECT date FROM traffic")
            mass = cursor.fetchall()
            i=0
            for i in range(len(mass)):
                dat2 = str(dat)
                dat4 = str(mass[i][0])

                if (dat2 < dat4):
                        print(dat4, "  -\n")
            else:
                pass
    
        print(  "\n") 
        
#####  ok
        if kolvo == 3:
            print("3- Выводим по периоду До указанной даты  \n")
            db = sqlite3.connect('base.db')
            cursor = db.cursor() 
            print("2- Введите дату для поиска После этой даты  \n")
            dat = str(input())
            dat1 = datetime.datetime.strptime(dat, '%Y-%m-%d %H:%M:%S')
            dat2=datetime
            dat4=datetime
            cursor.execute("SELECT date FROM traffic")

            mass = cursor.fetchall()
            i=0

            for i in range(len(mass)):
                dat2 = str(dat)
                dat4 = str(mass[i][0])

                if (dat2 > dat4):
                    print(dat4, "  -\n")
            else:
                pass

            print(  "\n") 


##### ok
        if kolvo == 4:
            print("4- Выводим по периоду в Указанный промежуток между 2 датами  \n")
            db = sqlite3.connect('base.db')
            cursor = db.cursor() 
            print("2- Введите дату #1  для поиска После этой даты  \n")
            dat11 = str(input())
            print("2- Введите дату #2  для поиска После этой даты  \n")
            dat12 = str(input())
        
     #      dat1 = datetime.datetime.strptime(dat, '%Y-%m-%d %H:%M:%S')
            dat2=datetime
            dat4=datetime
            cursor.execute("SELECT date FROM traffic")

            mass = cursor.fetchall()
            i=0

            for i in range(len(mass)):
                dat4 = str(mass[i][0])
                if ((dat11 < dat4) and (dat12 > dat4)):
                    print(dat4, "  -\n")
               
            else:
                pass

        print(  "\n") 




#####  ок
        if kolvo == 5:
            print("5- Выводим по IP адресу  \n")
            db = sqlite3.connect('base.db')
            cursor = db.cursor() 
            print("5- Введите IP адрес  \n")
            iip = str(input())
            cursor.execute("SELECT ip FROM traffic WHERE ip = ?", (iip,))
            results = str(cursor.fetchall())
            print(results,"\n")
            db.commit()
            db.close()
   

#######################################################################
# Создаем таблицу в базе - base.db
# по образцу из задания
def create():
    print("1- Into create func...")
    db = sqlite3.connect('base.db')
    cursor = db.cursor()    
    sql = u'''
    CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT KEY
    );
    '''
    db.execute(sql)
    db.commit()
    
    sql = u'''
    CREATE TABLE traffic (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER KEY,
    ip TEXT,
    date TEXT,
    received_traffic REAL
    );
    '''
    db.execute(sql)           
    db.commit()
    
#########
    sql = u''' INSERT INTO customers (
    customer_id, customer_name)
    VALUES
    (1, "John Doe"),
    (2, "Jane Smith"),
    (3, "Alice Johnson"),
    (4, "Bob Brown");
    '''
    db.execute(sql)
    db.commit()
#########
    sql = u''' INSERT INTO traffic (
    id, customer_id, ip, date, received_traffic)
    VALUES
    (101, 1, "192.168.218.159", "2022-01-05 10:15:00", 150.00),
    (102, 2, "192.168.5.110", "2022-07-15 13:45:00", 200.00),
    (103, 3, "192.168.214.201", "2022-02-25 18:30:00", 250.00),
    (104, 4, "192.168.224.118", "2024-03-07 12:00:00", 300.00),
    (105, 2, "192.168.218.159", "2024-03-15 14:00:00", 120.00),
    (106, 4, "192.168.5.110", "2024-03-18 15:00:00", 400.00),
    (107, 1, "192.168.214.201", "2023-01-10 10:30:00", 180.00),
    (108, 3, "192.168.224.118", "2023-02-28 14:00:00", 220.00),
    (109, 2, "192.168.218.159", "2023-03-01 16:15:00", 175.00),
    (110, 4, "192.168.5.110", "2023-03-10 17:45:00", 300.00),
    (111, 1, "192.168.214.201", "2023-03-20 13:00:00", 140.00),
    (112, 3, "192.168.224.118", "2024-03-22 09:00:00", 260.00),
    (113, 2, "192.168.218.159", "2024-03-25 15:30:00", 110.00),
    (114, 4, "192.168.5.110", "2024-04-01 12:00:00", 320.00),
    (115, 1, "192.168.214.201", "2024-04-05 11:15:00", 150.00),
    (116, 3, "192.168.224.118", "2023-04-08 14:45:00", 290.00),
    (117, 4, "192.168.214.201", "2023-04-10 16:30:00", 210.00),
    (118, 2, "192.168.224.118", "2025-04-12 18:00:00", 125.00),
    (119, 1, "192.168.218.159", "2025-04-15 12:30:00", 165.00),
    (120, 3, "192.168.214.201", "2025-04-18 14:15:00", 270.00),
    (121, 4, "192.168.224.118", "2025-04-20 10:45:00", 190.00),
    (122, 1, "192.168.218.159", "2025-04-22 09:30:00", 130.00),
    (123, 2, "192.168.224.118", "2025-04-25 11:00:00", 160.00),
    (124, 3, "192.168.218.159", "2026-04-28 14:00:00", 240.00),
    (125, 4, "192.168.214.201", "2026-04-30 17:15:00", 210.00),
    (126, 1, "192.168.224.118", "2026-05-02 13:45:00", 170.00);   
    '''
    db.execute(sql)
    db.commit()
    db.close()


####################################################################
if __name__ != "__main__":
    print("  The end... ")

if __name__ == "__main__":
   print("  Testovoe zadanie  ")
###########
# var


choice = int  # Выбор действия
###########
print("  Выберите действие: \n")
print("  1 - Создать базу \n")
print("  2 - Метод traffic для подсчета траффика за период \n")
print("  3 - Exit \n")
choice = int(input())
if choice == 1:
    create()
    
if choice == int(2):
    tr.traffic()
    
if choice == int(3):
    exit()



###########
# Конец
print(" End of program  ")
##################################################################
