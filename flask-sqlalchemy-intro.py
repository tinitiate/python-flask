## >---
## >title: Python SQLAlchemy ORM
## >metadata:
## >    description: 'Python SQLALCHEMY, ORM'
## >    keywords: 'Python SQLALCHEMY, ORM, example code, tutorials'
## >author: Venkata Bhattaram / tinitiate.com
## >code-alias: sqlalchemy
## >slug: python/modules/sqlalchemy
## >---

## ># Python SQL ALCHEMY ORM [Object Relationship Mapper]
## >* Data resides in a Database, and SQL must be used to perform basic 
## >  create, read, update and delete (CRUD) Operations.
## >* ORM [Object Relationship Mapper], Enables to perform DB CRUD operations
## >* Object Relational Mapper gives application developers the full power and 
## >  flexibility of SQL, Without actually using SQL.


## >## Python FLASK-SQLALCHEMY ORM [Object Relationship Mapping]
## >* Here we demonstrate the FLASK-SQLALCHEMY ORM
## >* Install the FLASK-SQLALCHEMY package using:
## >  `pip install flask-sqlalchemy`
## >* Flask-SQLAlchemy is an extension for Flask that adds support for 
## >  SQLAlchemy to your application. 
## >* It requires SQLAlchemy 0.6 or higher. It provides useful defaults and 
## >  extra helpers that make it easier to accomplish CRUD tasks.


## >```python

# Step 1.
# import flask-sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Import this to insert date data type into the database
from datetime import datetime


# Step 2. 
# Create a flask APP
app = Flask(__name__)

# Step 4. 
# 1. Create Flask application object and set the URI for the database 
# 2. Here we will be using flask sqlalchemy with Oracle 12c pdb
# 3. Use the TNSNAMES entry data for the PDB, for the Host Name, 
#    Port and Instance Name.

# Create the Connection String with TNS entry
l_oracle_conn_string = "oracle+cx_oracle://tinitiate:tinitiate@(DESCRIPTION =  (ADDRESS = (PROTOCOL = TCP) (HOST = 127.0.0.1) (PORT = 1521) ) (CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = pdborcl)    ))"

app.config['SQLALCHEMY_DATABASE_URI'] = l_oracle_conn_string     
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'false'
db = SQLAlchemy(app)


# Step 5.
# Create a Models or  Tables
# Also creating TWO tables with a foreign key relationship
# Define a table1: ti_emp
# With columns
# emp_id int and primary key
# emp_name varchar2(20)
# emp_join_date datatime
class ti_emp(db.Model):
    emp_id        = db.Column(db.Integer, primary_key=True)
    emp_name      = db.Column(db.String(20))
    emp_join_date = db.Column(db.DateTime)

    def __init__(self, emp_id, emp_name, emp_join_date):
       self.emp_id        = emp_id
       self.emp_name      = emp_name
       self.emp_join_date = emp_join_date

       
# Define a table2: ti_emp_sal
# With columns
# emp_sal_id  int and primary key
# emp_id      int and Foreign Key to TI_EMP.EMP_ID
# sal_month   varchar2(20)
# sal_year    int
class ti_emp_sal(db.Model):
    emp_sal_id  = db.Column(db.Integer, primary_key=True)
    emp_id      = db.Column(db.Integer, db.ForeignKey('ti_emp.emp_id'))
    sal_month   = db.Column(db.String(20))
    sal_year    = db.Column(db.Integer)
    
    def __init__(self, emp_sal_id, emp_id, sal_month, sal_year):
       self.emp_sal_id = emp_sal_id
       self.emp_id     = emp_id
       self.sal_month  = sal_month
       self.sal_year   = sal_year

 # Step 6.
 # create the tables


# Create all the tables
try:
    db.create_all()
    print("Tables ti_emp and ti_emp_sal created !")
except Exception as e:
    print(e)
    
## >```    


## >## FLASK-SQLALCHEMY Insert data into the tables
## >* "db.session.add" is used to insert data.
## >* Create the ROW data using the class of the table object.
## >* "db.session.add_all" is used to bluk insert data.
## >* Create the ROWs of data using the multiple DB table object.

## >```python

# Create a table object

# Insert One row at a time
# Here for datetime, we generate a specific Date time
l_ti_emp_row_data = ti_emp(1,'ABC',datetime.strptime('24052010', '%d%m%Y').date())
db.session.add(l_ti_emp_row_data)

# Here for datetime, we use system default Date time
l_ti_emp_row_data = ti_emp(2,'XYZ',datetime.utcnow())
db.session.add(l_ti_emp_row_data)


# Bulk Insert multiple rows
row1 = ti_emp(3,'DEF',datetime.utcnow())
row2 = ti_emp(4,'IJK',datetime.utcnow())
row3 = ti_emp(5,'LMN',datetime.utcnow())
row4 = ti_emp(6,'OPQ',datetime.utcnow())
row5 = ti_emp(7,'RST',datetime.utcnow())

# Bulk Insert all rows
db.session.add_all([row1, row2, row3, row4, row5])

# Commit the changes
db.session.commit()
## >```



## >## FLASK-SQLALCHEMY Select data from tables
## >* Below is the demonstration for data retrival of single and all rows:
## >* Get Single Row with a whare condition using the <table-name>.query.filter_by
## >* Get All Rows using the <table-name>.query.all

## >```python
# Get the ROW DATA from the ti_emp table, using the "db.session.query"
# row_data retrives all the row data for "ti_emp.emp_id == 1"
# row_data = db.session.query(ti_emp).filter(ti_emp.emp_id = 1)
# print(row_data)
row_data = ti_emp.query.filter_by(emp_id = 1).first()

# print individual row_data columns
print(row_data.emp_id)
print(row_data.emp_name)
print(row_data.emp_join_date)


# Get all rows of the table
all_rows_data = ti_emp.query.all()

for row in all_rows_data:
    print(row.emp_id, row.emp_name, row.emp_join_date)

## >```


## >## FLASK-SQLALCHEMY Update data in the tables
## >* For UPDATE of records, First we must Query the row(s) that need to be changed.
## >* Assign the new value to the retrived column value and perform a commit.
## >```python

# Process to perform UPDATE with flask-sqlalchemy

# STEP 1. Retrive the data
row_data = ti_emp.query.filter_by(emp_id = 1).first()


# STEP 2. Change the value of the row.column
# Displaying the current emp_name for emp_id = 1
print(row_data.emp_name) # ABC


# STEp 3. Assign a new Value
row_data.emp_name = 'TIN'

# STEP 4. Perform a commit
db.session.commit()

# Check for UPDATED value, by querying the table again
row_data = ti_emp.query.filter_by(emp_id = 1).first()
print(row_data.emp_name)

## >```



## >## FLASK-SQLALCHEMY Delete data from the tables
## >```python

# Retrive the data that is to be DELETED
row_data = ti_emp.query.filter_by(emp_id = 3).first()

# Display the ROW column values that will be deleted
print(row_data.emp_id)
print(row_data.emp_name)
print(row_data.emp_join_date)

# Perform the delete
db.session.delete(row_data)
db.session.commit()


# Check to confirm the row deletion
# Retrive data again
row_data = ti_emp.query.all()

# Print the current row data 
for row in row_data:
    print(row.emp_id, row.emp_name, row.emp_join_date)
## >```
