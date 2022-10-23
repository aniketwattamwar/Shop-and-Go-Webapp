from django.db import models
import pymysql

from django.core import serializers

conn = pymysql.connect(
        host= "awseb-e-84pdjvupzm-stack-awsebrdsdatabase-okcadrnpodya.cqbqeagztkxf.us-west-2.rds.amazonaws.com", #endpoint link
        port = 3306, # 3306
        user = 'admin', # admin
        password = 'adminadmin', #adminadmin
        db = 'ebdb', #test
        )

# Create your models here to push the data into RDS
def insert_details(firstname, lastname, email, password):
    cur=conn.cursor()
    cur.execute("INSERT INTO ebdb (firstname,lastname,email,password) VALUES (%s,%s,%s,%s)", (firstname, lastname, email, password))
    conn.commit()

def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM ebdb")
    details = cur.fetchall()
    return details

def get_product_data():
    cur=conn.cursor()
    cur.execute("SELECT * FROM product_data")
    product_data = cur.fetchall()
    return product_data



