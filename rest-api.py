## >---
## >title: Python Flask RESTful Web Services
## >metadata:
## >    description: 'python flask RESTful Web Services'
## >    keywords: 'python flask RESTful API, Web Services tutorials'
## >author: Venkata Bhattaram / tinitiate.com
## >code-alias: rest-web-services
## >slug: python/flask/rest-web-services
## >---

## ># WEB SERVICES
## >* APIs are Application Programming Interface is a subroutine or a method 
## >  or a function on a server.
## >* These APIs can be called remotely using a concept called WEB SERVICES.
## >* These web services are a means to have machine to machine communication, 
## >  through a standard means of representing information in JSON or XML formats.


## >## Python Flask RESTful APIs Web Services
## >* REST or REpresentational State Transfer is type of web serices architecture.
## >* The best part of RESTful Web Service is callable like a of URI, this is 
## >  it can be called like a HTTP call, with a URL ( Uniform Resource Identifier) 
## >  and supports the CRUD (Create, Read, Update and Delete) operations.
## >* A RESTful webservice is about delivering data and giving access to the  
## >  caller or a client program to perform CRUB using the following :
## >  1. GET    - Retrieve all records of data
## >  2. GET    - Retrieve a specific record of data
## >  3. POST   - Create a record
## >  4. PUT    - Update a record
## >  5. DELETE - Delete a record



## >```python
from flask import Flask, jsonify, request
app = Flask(__name__)



# Create some data, price_list for some products, 
# here we have a List of dictionaries
price_list=[
 {
 'prod_id':'1',
 'prod_name':'Apples',
 'price':'1.00'
 },
 {
 'prod_id':'2',
 'prod_name':'Oranges',
 'price':'2.00'
 },
 {
 'prod_id':'3',
 'prod_name':'Peaches',
 'price':'2.50'
 }
]


# This is the Route to the URL: 
# http://localhost:5000/price_data/prices
# Here we display the all the price_list data,
@app.route('/price_data/prices',methods=['GET'])
def get_all_prices():
    return jsonify({'price_data':price_list})
 

 
# This is the Route to the URL: 
# http://localhost:5000/price_data/price_of_product_name/
# Here we display the all the price_list data, by product_name
@app.route('/price_data/price_of_product_name/<product_name>', methods=['GET'])
def get_price_by_product_name(product_name):
    
    for price_data in price_list:
        if (price_data['prod_name'] == product_name):
            l_price = price_data
        
        
    return(l_price)
    # return jsonify({'Product Price':price})
 


# This is the Route to the URL: 
# http://localhost:5000/price_data/price_of_product_id/2
# Here we display the all the price_list data, by product_id
@app.route('/price_data/price_of_product_id/<product_id>', methods=['GET'])
def get_price_by_product_id(product_id):

    price = [price_data['price'] for price_data in price_list if price_data['prod_id'] == product_id]
    return jsonify({'Product Price':price})


    
# Same as above with different systax. 
# http://localhost:5000/price_data/price_of_product_id_syntax2/2
# Here we display the all the price_list data, by product_id
@app.route('/price_data/price_of_product_id_syntax2/<product_id>', methods=['GET'])
def get_price_by_product_id_syntax2(product_id):

    for price_data in price_list:
        if (price_data['prod_id'] == product_id):
            l_price = price_data['price']
        
        
    return jsonify({'Product Price':[l_price]})
    
    
if __name__ == '__main__':
   app.run(debug = True)    
## >```

