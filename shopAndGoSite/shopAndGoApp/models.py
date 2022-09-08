from django.db import models
import pymysql

from django.core import serializers



# conn = pymysql.connect(
#         host= "shopandgoregistration.cpskakpqkgvt.us-east-1.rds.amazonaws.com", #endpoint link
#         port = 3306, # 3306
#         user = 'admin', # admin
#         password = 'adminadmin', #adminadmin
#         db = 'shopandgoschema', #test
#         )

# Create your models here to push the data into RDS
# def insert_details(firstname, lastname, email, password):
#     cur=conn.cursor()
#     cur.execute("INSERT INTO registration_details (firstname,lastname,email,password) VALUES (%s,%s,%s,%s)", (firstname, lastname, email, password))
#     conn.commit()

# def get_details():
#     cur=conn.cursor()
#     cur.execute("SELECT *  FROM registration_details")
#     details = cur.fetchall()
#     return details



