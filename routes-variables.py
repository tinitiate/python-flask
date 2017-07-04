## >---
## >title: Python Flask routing variables
## >metadata:
## >    description: 'python flask routing variables'
## >    keywords: 'Python flask, routing variables, tutorials'
## >author: Venkata Bhattaram / tinitiate.com
## >code-alias: routing-variables
## >slug: python/flask/routing-variables
## >---

## >## Python Flask routing variables
## >* Routing is the method to display different content for every URL folder
## >* The "home page" localhost:5000, displays the default message
## >* It is possible to create any url path using varibles
## >* This is useful to create dynamic pages
## >* Save the below file as `routes-variables.py`
## >* At the command prompt run the program `python routes-variables.py`

## >```python
from flask import Flask, render_template
app = Flask(__name__)

# This is the home-page or the "localhost:5000"
@app.route("/")
def home():
# * Now open the localhost:5000
    return "<h4>Welcome to the Tinitiate HOME</h4>"
#   This will display the following message: "Welcome to the Tinitiate HOME"


# Creating a Routes    
# The following will create a static page
@app.route("/topic")
def topic():
    return "<h4>Welcome to the TOPIC page</h4>"
# * Now open the localhost:5000/topic
#   This will display the following message: "Welcome to the TOPIC page"
    

# Creating a variable URL route
# The following will create a page with the multiplication table of 
# the number specified and displays in the page:
@app.route('/tables/<num>')
def tables(num):
    
    l_mul_table = ""
    for c1 in range(10):
        l_mul_table = l_mul_table + '<br>' + str(num) + " X " + str(c1+1) + " = " + str(int(num)*(c1+1))
        
    return "<h4>Welcome to the " + num + " Table page</h4> <br> " + l_mul_table
# * Now open the localhost:5000/tables/5
#   This will display the following message: "Welcome to the 5 Table page"



# Creating a variable URL route
# The following will create a page with the multiplication table of 
# the number specified and displays in the page:
@app.route('/even_or_odd/<num>')
def even_or_odd(num):
    
    if(int(num)%2 == 0):
        return "Even or ODD: <h4>" + str(num) + " is EVEN </h4>"
    else:
        return "<h4>Even or ODD: " + str(num) + " is ODD </h4>"
        
# * Now open the localhost:5000/even_or_odd/5
#   This will display the following message: "Even or ODD: 5 is ODD"


    
if __name__ == '__main__':
   app.run(debug = True)    
## >```
