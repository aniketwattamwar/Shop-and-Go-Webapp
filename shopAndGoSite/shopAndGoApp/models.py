from webbrowser import get
from django.db import models
import pymysql

from django.core import serializers

conn = pymysql.connect(
        host= "ebdb.cpskakpqkgvt.us-east-1.rds.amazonaws.com", #endpoint link
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

def get_details(password):
    cur=conn.cursor()
    # query = "SELECT * FROM ebdb where email"
    cur.execute("SELECT * FROM ebdb where password=%s",(password))
    details = cur.fetchall()
    return details

def get_product_data():
    cur=conn.cursor()
    cur.execute("SELECT * FROM product_data")
    product_data = cur.fetchall()
    return product_data

def insert_address(user_id,address,order_id, product_id):
    cur=conn.cursor()
    cur.execute("INSERT INTO address (user_id, address,order_id,product_id) VALUES (%s,%s,%s,%s)", (user_id, address,order_id,product_id))
    conn.commit()

def add_payment(user_id, amount, order_id, name, cardnumber):
    cur=conn.cursor()
    cur.execute("INSERT INTO payment (user_id, amount, order_id, name, cardnumber) VALUES (%s,%s,%s,%s,%s)", (user_id, amount, order_id, name, cardnumber))
    conn.commit()


def get_address(user_id):
    cur=conn.cursor()
    cur.execute("SELECT * FROM address where user_id=%s",(user_id))
    get_address = cur.fetchall()
    return get_address

def get_payment(user_id):
    cur=conn.cursor()
    cur.execute("SELECT * FROM payment where user_id=%s",(user_id))
    get_payment = cur.fetchall()
    return get_payment

def get_ordered_product(product_id):
    cur=conn.cursor()
    cur.execute("SELECT * FROM product_data where product_id=%s",(product_id))
    get_ordered_product = cur.fetchall()
    return get_ordered_product

# CREATE TABLE `ebdb`.`product_data` (
#   `product_id` INT NOT NULL AUTO_INCREMENT,
#   `product_name` VARCHAR(45) NULL,
#   `product_price` VARCHAR(45) NULL,
#   `product_img` VARCHAR(45) NULL,
#   PRIMARY KEY (`product_id`));


# INSERT INTO `ebdb`.`product_data` (`pid`, `product_name`, `product_price`, `product_img`) VALUES ('1', 'iphone 8', '299', '/static/img/iphone.png');
# INSERT INTO `ebdb`.`product_data` (`pid`, `product_name`, `product_price`, `product_img`) VALUES ('2', 'iphone X', '399', '/static/img/iphone.png');
# INSERT INTO `ebdb`.`product_data` (`pid`, `product_name`, `product_price`, `product_img`) VALUES ('3', 'iphone 12', '499', '/static/img/iphone.png');
# INSERT INTO `ebdb`.`product_data` (`pid`, `product_name`, `product_price`, `product_img`) VALUES ('4', 'iphone 13', '599', '/static/img/iphone.png');
# INSERT INTO `ebdb`.`product_data` (`pid`, `product_name`, `product_price`, `product_img`) VALUES ('5', 'iphone 13 mini', '699', '/static/img/iphone.png');

# CREATE TABLE `ebdb`.`orders` (
#   `order_id` INT NOT NULL AUTO_INCREMENT,
#   `product_name` VARCHAR(45) NULL,
#   `product_id` VARCHAR(45) NULL,
#   `user_id` VARCHAR(45) NULL,
#   `product_price` VARCHAR(45) NULL,
#   PRIMARY KEY (`order_id`));


# CREATE TABLE `ebdb`.`ebdb` (
#   `user_id` INT NOT NULL AUTO_INCREMENT,
#   `firstname` VARCHAR(45) NULL,
#   `lastname` VARCHAR(45) NULL,
#   `email` VARCHAR(45) NULL,
#   `password` VARCHAR(45) NULL,
#   PRIMARY KEY (`user_id`));

# CREATE TABLE `ebdb`.`address` (
#   `address_id` INT NOT NULL AUTO_INCREMENT,
#   `address` VARCHAR(45) NULL,
#   `user_id` VARCHAR(45) NULL,
#   `order_id` VARCHAR(45) NULL,
#   `product_id` VARCHAR(45) NULL,
#   PRIMARY KEY (`address_id`));

# CREATE TABLE `ebdb`.`payment` (
#   `payment_id` INT NOT NULL AUTO_INCREMENT,
#   `user_id` INT NULL,
#   `amount` INT NULL,
#   `order_id` INT NULL,
#   `name` VARCHAR(45) NULL,
#   PRIMARY KEY (`payment_id`));
