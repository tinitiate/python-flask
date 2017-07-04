## >---
## >title: Python HTTP methods
## >metadata:
## >    description: 'Python HTTP methods'
## >    keywords: 'Python HTTP methods, tutorials'
## >author: Venkata Bhattaram / tinitiate.com
## >code-alias: HTTP-methods
## >slug: python/flask/http-methods
## >---

## >## Python Flask HTTP (POST - GET) methods
## >* HTTP supports TWO methods to send data to server side entities and
## >  get response back from the same. 
## >* Both POST and GET are the SAME, they can be used to retrive, update and 
## >* delete information on the server using HTTP.
## >* Both POST and GET must be sent to a server side call, in this case a
## >  script with Python Flask code.
## >
## >* **POST** 
## >* POST submits data to the server usually from a form.
## >* POST requests MUST not be used when changing data at the server
## >* Use POST to send secure data such as passwords
## >* POST supports sending large amounts of data
## >* POST for creating / editing information.
## >
## >* **GET**
## >* GET returns response data from server.
## >* GET Must be ideally used for retrieving / viewing information 


## >```python
from flask import Flask, redirect, url_for, request
app = Flask(__name__)


# Create a FORM on the homepage, Here we enter a number to get its
# multiplication table,
# There are TWO forms one sending data using POST and Other form receiving data
# on the server side by GET.
@app.route('/')
def index():
    return """<html>
   <body>

      <form action = "http://localhost:5000/tables" method = "post">
         <p>Enter a number for printing its Multiplication table:</p>
         <p><input type = "text" name = "num_box" /></p>
         <p><input type = "submit" value = "POST DEMO" /></p>
      </form>

      <form action = "http://localhost:5000/tables" method = "get">
         <p>Enter a number for printing its Multiplication table:</p>
         <p><input type = "text" name = "num_box" /></p>
         <p><input type = "submit" value = "GET DEMO" /></p>
      </form>

   </body>
</html>"""


# This method is called by both the forms, and for POST and GET the data will
# be called / received as per POST or GET.
@app.route('/tables',methods = ['POST', 'GET'])
def tables():
    if request.method == 'POST':
        num = request.form['num_box']

        l_mul_table = ""
        for c1 in range(10):
            l_mul_table = l_mul_table + '<br>'\
                        + str(num) + " X " \
                        + str(c1+1) + " = " \
                        + str(int(num)*(c1+1))

        return "<h4>Welcome to the " + num + " Table page by POST method</h4> <br> " + l_mul_table

    else:
        num = request.args.get('num_box')

        l_mul_table = ""
        for c1 in range(10):
            l_mul_table = l_mul_table + '<br>' + str(num) + " X " + str(c1+1) + " = " + str(int(num)*(c1+1))

        return "<h4>Welcome to the " + num + " Table page by GET method</h4> <br> " + l_mul_table

    # * This will route the webpage to localhost:5000/tables

if __name__ == '__main__':
   app.run(debug = True)

## >```