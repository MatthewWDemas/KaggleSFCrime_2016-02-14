#!/usr/bin/python3
#make_mysql_db_from_csv.py
#take data file from kaggle training dataset and insert it into mysql
#code adapted from:
#http://stackoverflow.com/questions/10154633/load-csv-data-into-mysql-in-python

import csv
import mysql.connector
from mysql.connector import errorcode
MYSQLUSER = 'root'

#---------------------------------
#CREATE DATABASE IF DOESN'T EXIST
#code from:
#https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html

cnx = mysql.connector.connect(user=MYSQLUSER)
cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format('kaggle_sf'))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx.database = 'kaggle_sf'
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = 'kaggle_sf'
    else:
        print(err)
        exit(1)
#---------------------------------

#CREATE TABLE
try:
    cursor.execute(#I never remember how to make this span several lines
        "CREATE TABLE IF NOT EXISTS train(id INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(id), dates VARCHAR(256),category VARCHAR(256),descript VARCHAR(256),dayofweek VARCHAR(256),pddistrict VARCHAR(256),resolution VARCHAR(256),address VARCHAR(256),x VARCHAR(256),y VARCHAR(256))")
except mysql.connector.Error as err:
    print("Failed creating table: {}".format(err))
    exit(1)


#CHECK IF TABLE HAS ROWS
results = cursor.execute("""SELECT count(*) FROM train""")
if not results:
    print("Table was empty")



#ADD DATA FROM train.csv TO TABLE
cursor.execute("LOAD DATA LOCAL INFILE 'train.csv' INTO TABLE train")
#close the connection to the database.
cursor.close()
