## >---
## >title: Python SQLAlchemy ORM Queries
## >metadata:
## >    description: 'Python SQLALCHEMY, ORM Queries'
## >    keywords: 'Python SQLALCHEMY, ORM, SELECT, GROUP BY, CASE STATEMENT example code, tutorials'
## >author: Venkata Bhattaram / tinitiate.com
## >code-alias: sqlalchemy-queries
## >slug: python/modules/sqlalchemy-queries
## >---

## ># Python SQL ALCHEMY ORM [Object Relationship Mapper] Queries
## >* In this program we demonstrate various SQL-Query operations
## >  Such as JOINs, Group By, Case Statement, Limiting Data

## >## Prepare tables and rows for the demonstration

## >* Define a table1: ti_dept
## >    * With columns
## >    * dept_id     int and primary key
## >    * dept_name   varchar2(20)

## >* Define a table2: ti_emp
## >    * With columns
## >    * emp_id        int and primary key
## >    * dept_id       int and Foreign Key to TI_DEPT.DEPT_ID
## >    * emp_name      varchar2(20)
## >    * emp_join_date datatime

## >* Define a table3: ti_emp_sal
## >    * With columns
## >    * emp_sal_id  int and primary key
## >    * emp_id      int and Foreign Key to TI_EMP.EMP_ID
## >    * sal_month   varchar2(20)
## >    * sal_year    int


## >```python

# Step 1.
# import flask-sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Import this to insert date data type into the database
from datetime import datetime

from sqlalchemy.sql import func,case, literal_column, select

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

# Define a table1: ti_dept
# With columns
# dept_id     int and primary key
# dept_name   varchar2(20)
class ti_dept(db.Model):
    dept_id        = db.Column(db.Integer, primary_key=True)
    dept_name      = db.Column(db.String(20))

    def __init__(self, dept_id, dept_name):
       self.dept_id   = dept_id
       self.dept_name = dept_name


# Define a table2: ti_emp
# With columns
# emp_id int and primary key
# emp_name varchar2(20)
# emp_join_date datatime
class ti_emp(db.Model):
    emp_id        = db.Column(db.Integer, primary_key=True)
    dept_id       = db.Column(db.Integer, db.ForeignKey('ti_dept.dept_id'))
    emp_name      = db.Column(db.String(20))
    emp_sal       = db.Column(db.Integer)
    emp_join_date = db.Column(db.DateTime)

    def __init__(self, emp_id, dept_id, emp_name, emp_sal, emp_join_date):
       self.emp_id        = emp_id
       self.dept_id       = dept_id
       self.emp_name      = emp_name
       self.emp_sal       = emp_sal
       self.emp_join_date = emp_join_date


# Define a table3: ti_emp_sal
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
    print("Tables ti_dept, ti_emp and ti_emp_sal created !")
except Exception as e:
    print(e)

## >```

## >## FLASK-SQLALCHEMY Insert data into the tables
## >* "db.session.add_all" is used to bluk insert data.
## >* Create the ROWs of data using the multiple DB table object.

## >```python
try:
    # Bulk Insert rows into ti_dept
    row1 = ti_dept(1,'SALES')
    row2 = ti_dept(2,'IT')
    row3 = ti_dept(3,'ADMIN')

    # Bulk Insert all rows
    db.session.add_all([row1, row2, row3])

    # Commit the changes
    db.session.commit()

except Exception as e:
    print(e)
    # Commit the changes
    db.session.rollback()



# Bulk Insert rows into ti_emp
try:
    row1 = ti_emp(1,1,'ABC',7000,datetime.utcnow())
    row2 = ti_emp(2,2,'PQR',6500,datetime.utcnow())
    row3 = ti_emp(3,2,'DEF',6000,datetime.utcnow())
    row4 = ti_emp(4,1,'IJK',7500,datetime.utcnow())
    row5 = ti_emp(5,3,'LMN',9000,datetime.utcnow())
    row6 = ti_emp(6,2,'PQR',10000,datetime.utcnow())
    row7 = ti_emp(7,2,'TIN',8000,datetime.utcnow())
    
    # Bulk Insert all rows
    db.session.add_all([row1, row2, row3, row4, row5, row6, row7])

    # Commit the changes
    db.session.commit()
except Exception as e:
    # Commit the changes
    db.session.rollback()
    print(e)




# Bulk Insert rows into ti_emp
try:
    row1 = ti_emp_sal(1,1,'JAN',2010)
    row2 = ti_emp_sal(2,2,'JAN',2010)
    row3 = ti_emp_sal(3,3,'JAN',2010)
    row4 = ti_emp_sal(4,4,'JAN',2010)
    row5 = ti_emp_sal(5,5,'JAN',2010)
    row6 = ti_emp_sal(6,6,'JAN',2010)
    #
    row7 = ti_emp_sal(7,1,'FEB',2010)
    row8 = ti_emp_sal(8,2,'FEB',2010)
    row9 = ti_emp_sal(9,3,'FEB',2010)
    row10 = ti_emp_sal(10,4,'FEB',2010)
    row11 = ti_emp_sal(11,5,'FEB',2010)
    row12 = ti_emp_sal(12,6,'FEB',2010)
    #
    row13 = ti_emp_sal(13,1,'MAR',2010)
    row14 = ti_emp_sal(14,2,'MAR',2010)
    row15 = ti_emp_sal(15,3,'MAR',2010)
    row16 = ti_emp_sal(16,4,'MAR',2010)
    row17 = ti_emp_sal(17,5,'MAR',2010)
    row18 = ti_emp_sal(18,6,'MAR',2010)

    # Bulk Insert all rows
    db.session.add_all([row1, row2, row3, row4, row5, row6])
    db.session.add_all([row7, row8, row9, row10, row11, row12])
    db.session.add_all([row13, row14, row15, row16, row17, row18])

    # Commit the changes
    db.session.commit()

except Exception as e:
    # Commit the changes
    db.session.rollback()

## >```


## >## FLASK-SQLALCHEMY Select single and All Rows from all tables
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


## >## FLASK-SQLALCHEMY Select by specifying column names from a table
## >```python
# Select ONLY emp_id and emp_name from ti_emp
result = ti_emp.query.with_entities(ti_emp.emp_id, ti_emp.emp_name)
for row in result:
    print(row.emp_id, row.emp_name)
## >```


## >## FLASK-SQLALCHEMY DISTINCT, COUNT, IN, NOT IN clause queruy on table
## >* Make sure to import "from sqlalchemy.sql import func"

## >```python
from sqlalchemy.sql import func

# DISTINCT emp_id from ti_emp_sal table
distinct_data = ti_emp_sal.query.with_entities(ti_emp_sal.emp_id).distinct(ti_emp_sal.emp_id)

for row in distinct_data:
    print(row.emp_id)

# Get count of all rows
l_rows = db.session.query(ti_emp).count()
print("Rows in TI_EMP table:",l_rows)

# Get count of rows with JAN month in ti_emp_sal
l_rows = db.session.query(ti_emp_sal).filter(ti_emp_sal.sal_month == 'JAN').count()
print("JAN sal_month Rows in TI_EMP_SQL table:",l_rows)


# IN CLAUSE: Get count of rows with JAN and FEB months in ti_emp_sal
l_rows = db.session.query(ti_emp_sal).filter(ti_emp_sal.sal_month.in_(('JAN','FEB'))).count()
print("JAN and FEB sal_month Rows in TI_EMP_SQL table:",l_rows)


# NOT IN CLAUSE: Get count of rows with JAN and FEB months in ti_emp_sal
l_rows = db.session.query(ti_emp_sal).filter(~ti_emp_sal.sal_month.in_(('JAN','FEB'))).count()
print("Exclude JAN and FEB sal_month Row count in TI_EMP_SQL table:",l_rows)

## >```


## >## FLASK-SQLALCHEMY sum, avg, count, max, group_by
## >```python

l_count = db.session.query(func.count(ti_emp_sal.emp_id).label('emp_id_count'), ti_emp_sal.emp_id ).group_by(ti_emp_sal.emp_id).all()

for row in l_count:
    print(row.emp_id,row.emp_id_count)

# Get Max Salary Value in every dept_id
l_max = db.session.query(func.max(ti_emp.emp_sal).label('max_sal'), ti_emp.dept_id ).group_by(ti_emp.dept_id).all()

for row in l_max:
    print(row.dept_id,row.max_sal)

# Get Min Salary Value in every dept_id
l_min = db.session.query(func.min(ti_emp.emp_sal).label('min_sal'), ti_emp.dept_id ).group_by(ti_emp.dept_id).all()

for row in l_min:
    print(row.dept_id,row.min_sal)


# Get Sum of total Salary by dept_id
l_sum = db.session.query(func.sum(ti_emp.emp_sal).label('sal_sum'), ti_emp.dept_id ).group_by(ti_emp.dept_id).all()

for row in l_sum:
    print(row.dept_id,row.sal_sum)


# Get Avg of Salary by dept_id
l_avg = db.session.query(func.avg(ti_emp.emp_sal).label('sal_avg'), ti_emp.dept_id ).group_by(ti_emp.dept_id).all()

for row in l_avg:
    print(row.dept_id,row.sal_avg)

## >```


## >## FLASK-SQLALCHEMY JOIN or the INNER-JOIN
## >* JOINs are implemented by 
## >  <table-name-1>.query.join(<table-name-2>, tn1.column-name == tn2.column-name
## >* The ".add_columns" are the columns from the joined tables that are to be 
## >  displayed as part of the select.
## >```python

emp_details = ti_emp.query\
              .join(ti_emp_sal, ti_emp.emp_id==ti_emp_sal.emp_id)\
              .add_columns(ti_emp.emp_id, ti_emp.emp_name)

# Print the data
for row in emp_details:
    print(row.emp_id,row.emp_name)

## >```


## >## FLASK-SQLALCHEMY OUTER JOIN
## >* The FULL OUTER JOIN returns all rows from the both the joined tables.
## >* Below is the demonstration of Outer Join
## >```python
emp_details = ti_emp.query\
              .outerjoin(ti_emp_sal, ti_emp.emp_id==ti_emp_sal.emp_id)\
              .add_columns(ti_emp.emp_id, ti_emp.emp_name, ti_emp_sal.emp_sal_id)

# Print the data
for row in emp_details:
    print(row.emp_id, row.emp_name, row.emp_sal_id)
## >```


## >## FLASK-SQLALCHEMY LEFT JOIN
## >* The LEFT JOIN keyword returns all rows from the left table (table1),
## >  with the matching rows in the right table (table2).
## >* Below is the demonstration of Left Join
## >```python
emp_details = ti_emp_sal.query\
              .outerjoin(ti_emp, ti_emp.emp_id==ti_emp_sal.emp_id)\
              .add_columns(ti_emp.emp_id, ti_emp.emp_name, ti_emp_sal.emp_sal_id)\
              .filter(ti_emp_sal.emp_id == None)

# Print the data
for row in emp_details:
    print(row.emp_id, row.emp_name, row.emp_sal_id)
## >```


## >## FLASK-SQLALCHEMY Select CASE statement
## >* CASE Statement is used to substitute the column-value to other 
## >  literals based on a condition.
## >```python
## >* Here we change the values of sal_month, if the value is 
## >  JAN change to JANUARY, FEB to FEBRUARY ..
      
row_output = ti_emp_sal.query.with_entities(case([(ti_emp_sal.sal_month == 'JAN', 'JANUARY'),
               (ti_emp_sal.sal_month == 'FEB', 'FEBRUARY'),
               (ti_emp_sal.sal_month == 'MAR', 'MARCH')
              ],
              else_ = ti_emp_sal.sal_month).label('full_month_name'))


for l_data in row_output:
    print (l_data.full_month_name)
## >```


## >## FLASK-SQLALCHEMY ORDER BY statement
## >* ORDER BY Clause in SQL orders the output data or the data from the "select"
## >  Clause in the ASCENDING or DESCENDING order of your choice.
## >* In FLASK-SQLALCHEMY we can do that by using the following syntax;
## >* **MAKE SURE .all() is AFTER ORDER BY**
## >```python

# ORDER BY ASCENDING ORDER
all_rows_data = ti_emp.query.order_by(ti_emp.emp_name).all()

for row in all_rows_data:
    print(row.emp_id, row.emp_name, row.emp_join_date)

    
# ORDER BY DESCENDING ORDER    
all_rows_data = ti_emp.query.order_by(ti_emp.emp_name.desc()).all()

for row in all_rows_data:
    print(row.emp_id, row.emp_name, row.emp_join_date)
    
## >```
